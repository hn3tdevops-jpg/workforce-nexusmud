import re

with open("/home/workspace/workforce-nexusmud/packages/world_engine/engine.py", "r") as f:
    content = f.read()

# We want to replace from 'if action == "look"' to the end of process_command.
start_idx = content.find('        if action == "look" or action == "l":')

# We find the end of process_command (which is basically the end of the file in the current structure)
# We will just replace everything from start_idx to the end of the file with our new logic

new_logic = """        if action == "look" or action == "l":
            db = SessionLocal()
            room = db.query(RoomData).filter(RoomData.id == current_room).first()
            items_here = db.query(Item).filter(Item.room_id == current_room).all()
            db.close()
            players_here = self.get_players_in_room(current_room)
            others = [p for p in players_here if p != player_id]
            desc = f"[{room.name}]\\n{room.description}"
            
            if items_here:
                desc += f"\\nItems here: {', '.join([i.name for i in items_here])}"
                
            npcs_here = self.npc_manager.get_npcs_in_room(current_room)
            if npcs_here:
                desc += f"\\nNPCs here: {', '.join([npc.name for npc in npcs_here])}"
                
            if others:
                desc += f"\\nAlso here: {', '.join(others)}"
            return desc, None, None

        elif action in ["inventory", "inv", "i"]:
            db = SessionLocal()
            items = db.query(Item).filter(Item.owner_id == player_id).all()
            db.close()
            if items:
                inv = "\\n".join([f"- {i.name}" for i in items])
                return f"You are carrying:\\n{inv}", None, None
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
                player_resp += "\\n" + "\\n".join(npc_responses)
                
            broadcast_msg = f"{player_id} says: '{args}'"
            if npc_responses:
                broadcast_msg += "\\n" + "\\n".join(npc_responses)
                
            return player_resp, broadcast_msg, players_here

        elif action == "quests":
            db = SessionLocal()
            quests = db.query(Quest).filter(Quest.player_id == player_id).all()
            db.close()
            if not quests:
                return "You have no active quests.", None, None
            out = "Your Quests:\\n"
            for q in quests:
                status = "[Completed]" if q.is_completed else "[Active]"
                out += f"{status} {q.title}: {q.description}\\n"
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
                out = "Guilds:\\n" + "\\n".join([f"- {g.name}: {g.description}" for g in guilds])
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
            out = "Recent Memories:\\n" + "\\n".join([f"- {e.event_type}: {e.description}" for e in events])
            return out, None, None

        elif action in ["go", "move", "north", "south", "n", "s"]:
            # Simple hardcoded map for prototype
            moves = {
                "town_square": {"north": "north_gate", "n": "north_gate", "south": "south_alley", "s": "south_alley"},
                "north_gate": {"south": "town_square", "s": "town_square"},
                "south_alley": {"north": "town_square", "n": "town_square"}
            }
            
            direction = args if action in ["go", "move"] else action
            
            if direction in moves.get(current_room, {}):
                new_room_id = moves[current_room][direction]
                
                self.record_memory(player_id, "moved", f"Moved to {new_room_id}")
                
                # Move player
                db = SessionLocal()
                db_player = db.query(PlayerAccount).filter(PlayerAccount.id == player_id).first()
                db_player.room_id = new_room_id
                db.commit()
                db.close()
                
                # Look in new room
                look_response, _, _ = self.process_command(player_id, "look")
                
                return f"You head {direction}.\\n\\n{look_response}", None, None
            else:
                return "You can't go that way.", None, None

        elif action == "help":
            return "Commands: look, i/inv, take/drop <item>, say <msg>, go <direction>, quests, guild <list/join>, rep, memory, help", None, None

        else:
            return "Unknown command. Type 'help' for a list of commands.", None, None
"""

new_content = content[:start_idx] + new_logic
with open("/home/workspace/workforce-nexusmud/packages/world_engine/engine.py", "w") as f:
    f.write(new_content)
print("Patched engine.py")
