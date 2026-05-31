from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Tuple, List, Optional
import os

from packages.agent_core.npc import NPCManager
from packages.economy.models import Trade
from packages.territory.models import Territory
from packages.world_engine.graph import WorldGraph

Base = declarative_base()

class PlayerAccount(Base):
    __tablename__ = 'players'
    id = Column(String, primary_key=True)
    room_id = Column(String, nullable=False, default="town_square")
    reputation_score = Column(Integer, default=0)

class RoomData(Base):
    __tablename__ = 'rooms'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(String, ForeignKey('players.id'), nullable=True)
    room_id = Column(String, ForeignKey('rooms.id'), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Guild(Base):
    __tablename__ = 'guilds'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class GuildMember(Base):
    __tablename__ = 'guild_members'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(String, ForeignKey('players.id'), nullable=False)
    guild_id = Column(String, ForeignKey('guilds.id'), nullable=False)
    rank = Column(String, default="Member")

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(String, ForeignKey('players.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Integer, default=0) # 0=False, 1=True

class MemoryEvent(Base):
    __tablename__ = 'memory_events'
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_id = Column(String, nullable=False) # player_id or npc_id
    event_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    timestamp = Column(String, nullable=True)

# Setup SQLite
DB_PATH = "sqlite:///nexusmud.db"
engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class WorldEngine:
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self._seed_rooms()
        self.npc_manager = NPCManager()
        self.world_graph = WorldGraph()
        
    def _seed_rooms(self):
        db = SessionLocal()
        if not db.query(RoomData).filter(RoomData.id == "town_square").first():
            db.add(RoomData(id="town_square", name="Town Square", description="A bustling town square. Paths lead north and south."))
            db.add(RoomData(id="north_gate", name="North Gate", description="The northern gate of the town. You see guards standing watch."))
            db.add(RoomData(id="south_alley", name="South Alley", description="A dark, narrow alley to the south."))
            
            db.add(Guild(id="merchants_guild", name="The Merchant's Guild", description="A collective of traders and artisans."))
            db.add(Guild(id="guards_guild", name="The Town Guard", description="Protectors of the realm."))
            
            db.add(Item(room_id="town_square", name="rusty sword", description="An old rusty sword left behind."))
            db.add(Item(room_id="south_alley", name="shadow cloak", description="A dark cloak that blends into shadows."))
            
            db.commit()
        db.close()

    def record_memory(self, entity_id: str, event_type: str, description: str):
        from datetime import datetime
        db = SessionLocal()
        event = MemoryEvent(
            entity_id=entity_id, 
            event_type=event_type, 
            description=description,
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(event)
        db.commit()
        db.close()

    def get_or_create_player(self, player_id: str) -> PlayerAccount:
        db = SessionLocal()
        player = db.query(PlayerAccount).filter(PlayerAccount.id == player_id).first()
        if not player:
            player = PlayerAccount(id=player_id, room_id="town_square")
            db.add(player)
            db.commit()
            db.refresh(player)
        db.close()
        return player

    def get_players_in_room(self, room_id: str) -> List[str]:
        db = SessionLocal()
        players = db.query(PlayerAccount).filter(PlayerAccount.room_id == room_id).all()
        db.close()
        return [p.id for p in players]

    def player_connect(self, player_id: str) -> Tuple[str, List[str]]:
        player = self.get_or_create_player(player_id)
        db = SessionLocal()
        room = db.query(RoomData).filter(RoomData.id == player.room_id).first()
        db.close()
        
        room_desc = f"[{room.name}]
{room.description}"
        players_here = self.get_players_in_room(player.room_id)
        
        return f"Welcome to NexusMUD!

{room_desc}", players_here

    def player_disconnect(self, player_id: str) -> List[str]:
        player = self.get_or_create_player(player_id)
        return self.get_players_in_room(player.room_id)

    def process_command(self, player_id: str, command: str) -> Tuple[str, Optional[str], Optional[List[str]]]:
        """
        Returns (response_to_player, broadcast_message, list_of_targets)
        """
        cmd = command.strip().lower()
        parts = cmd.split(" ", 1)
        action = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        player = self.get_or_create_player(player_id)
        current_room = player.room_id

        if action == "look" or action == "l":
            db = SessionLocal()
            room = db.query(RoomData).filter(RoomData.id == current_room).first()
            items_here = db.query(Item).filter(Item.room_id == current_room).all()
            db.close()
            players_here = self.get_players_in_room(current_room)
            others = [p for p in players_here if p != player_id]
            desc = f"[{room.name}]
{room.description}"
            
            if items_here:
                desc += f"
Items here: {', '.join([i.name for i in items_here])}"
                
            npcs_here = self.npc_manager.get_npcs_in_room(current_room)
            if npcs_here:
                desc += f"
NPCs here: {', '.join([npc.name for npc in npcs_here])}"
                
            if others:
                desc += f"
Also here: {', '.join(others)}"
            return desc, None, None

        elif action in ["inventory", "inv", "i"]:
            db = SessionLocal()
            items = db.query(Item).filter(Item.owner_id == player_id).all()
            db.close()
            if items:
                inv = "
".join([f"- {i.name}" for i in items])
                return f"You are carrying:
{inv}", None, None
            return "You are not carrying anything.", None, None

        elif action == "take":
            if not args:
                return "Take what?", None, None
            db = SessionLocal()
            item = db.query(Item).filter(Item.room_id == current_room, Item.name == args).first()
            if item:
                item.room_id = None
                item.owner_id = player_id
                db.commit()
                db.close()
                self.record_memory(player_id, "item_taken", f"Took {args} from {current_room}")
                return f"You pick up the {args}.", f"{player_id} picks up a {args}.", self.get_players_in_room(current_room)
            db.close()
            return f"There is no {args} here.", None, None

        elif action == "drop":
            if not args:
                return "Drop what?", None, None
            db = SessionLocal()
            item = db.query(Item).filter(Item.owner_id == player_id, Item.name == args).first()
            if item:
                item.owner_id = None
                item.room_id = current_room
                db.commit()
                db.close()
                self.record_memory(player_id, "item_dropped", f"Dropped {args} in {current_room}")
                return f"You drop the {args}.", f"{player_id} drops a {args}.", self.get_players_in_room(current_room)
            db.close()
            return f"You don't have a {args}.", None, None

        elif action == "say":
            if not args:
                return "Say what?", None, None
            players_here = self.get_players_in_room(current_room)
            
            self.record_memory(player_id, "speak", f"Said: '{args}'")
            
            # Let NPCs respond
            npc_responses = self.npc_manager.handle_interaction(current_room, player_id, args)
            
            player_resp = f"You say: '{args}'"
            if npc_responses:
                player_resp += "
" + "
".join(npc_responses)
                
            broadcast_msg = f"{player_id} says: '{args}'"
            if npc_responses:
                broadcast_msg += "
" + "
".join(npc_responses)
                
            return player_resp, broadcast_msg, players_here

        elif action == "quests":
            db = SessionLocal()
            quests = db.query(Quest).filter(Quest.player_id == player_id).all()
            db.close()
            if not quests:
                return "You have no active quests.", None, None
            out = "Your Quests:
"
            for q in quests:
                status = "[Completed]" if q.is_completed else "[Active]"
                out += f"{status} {q.title}: {q.description}
"
            return out.strip(), None, None

        elif action == "guild":
            if not args:
                return "Guild commands: guild list, guild join <name>", None, None
            sub = args.split(" ", 1)
            subcmd = sub[0]
            db = SessionLocal()
            if subcmd == "list":
                guilds = db.query(Guild).all()
                db.close()
                if not guilds:
                    return "No guilds found.", None, None
                out = "Guilds:
" + "
".join([f"- {g.name}: {g.description}" for g in guilds])
                return out, None, None
            elif subcmd == "join" and len(sub) > 1:
                gname = sub[1]
                guild = db.query(Guild).filter(Guild.name.ilike(f"%{gname}%")).first()
                if not guild:
                    db.close()
                    return "No such guild.", None, None
                existing = db.query(GuildMember).filter(GuildMember.player_id == player_id, GuildMember.guild_id == guild.id).first()
                if existing:
                    db.close()
                    return f"You are already in {guild.name}.", None, None
                db.add(GuildMember(player_id=player_id, guild_id=guild.id))
                
                # Give rep bonus
                db_player = db.query(PlayerAccount).filter(PlayerAccount.id == player_id).first()
                db_player.reputation_score += 10
                
                db.commit()
                db.close()
                self.record_memory(player_id, "guild_joined", f"Joined {guild.name}")
                return f"You have joined {guild.name}! (+10 Rep)", f"{player_id} joined {guild.name}.", self.get_players_in_room(current_room)
            else:
                db.close()
                return "Invalid guild command.", None, None

        elif action in ["reputation", "rep"]:
            return f"Your reputation score is: {player.reputation_score}", None, None

        elif action == "memory":
            db = SessionLocal()
            events = db.query(MemoryEvent).filter(MemoryEvent.entity_id == player_id).order_by(MemoryEvent.id.desc()).limit(5).all()
            db.close()
            if not events:
                return "You have no memories.", None, None
            out = "Recent Memories:
" + "
".join([f"- {e.event_type}: {e.description}" for e in events])
            return out, None, None
