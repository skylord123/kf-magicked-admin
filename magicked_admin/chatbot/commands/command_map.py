from chatbot.commands.event_commands import *
from chatbot.commands.info_commands import *
from chatbot.commands.player_commands import *
from chatbot.commands.server_commands import *


class CommandMap:
    def __init__(self, server, chatbot):
        self.server = server
        self.chatbot = chatbot
        self.command_map = self.generate_map()

    def generate_map(self):
        wave_event_manager = CommandOnWaveManager(self.server, self.chatbot)
        trader_event_manager = CommandOnTraderManager(self.server, self.chatbot)
        time_event_manager = CommandOnTimeManager(self.server, self.chatbot)

        command_map = {
            'player_join': CommandGreeter(self.server),
            'stop_wc': wave_event_manager,
            'start_wc': wave_event_manager,
            'new_wave': wave_event_manager,
            'start_tc': time_event_manager,
            'stop_tc': time_event_manager,
            'start_trc': trader_event_manager,
            'stop_trc': trader_event_manager,
            't_close': trader_event_manager,
            't_open': trader_event_manager,
            'record_wave': CommandHighWave(self.server, admin_only=False),
            'enforce_levels': CommandEnforceLevels(self.server),
            'enforce_dosh': CommandEnforceDosh(self.server),
            'say': CommandSay(self.server),
            'restart': CommandRestart(self.server),
            'load_map': CommandLoadMap(self.server),
            'password': CommandPassword(self.server),
            'silent': CommandSilent(self.server, self.chatbot),
            'run': CommandRun(self.server, self.chatbot),
            'length': CommandLength(self.server),
            'difficulty': CommandDifficulty(self.server),
            'game_mode': CommandGameMode(self.server),
            'players': CommandPlayers(self.server, admin_only=False),
            'game': CommandGame(self.server, admin_only=False),
            'help': CommandHelp(self.server, admin_only=False),
            'kills': CommandKills(self.server, admin_only=False),
            'kick': CommandKick(self.server, admin_only=True),
            'ban': CommandBan(self.server, admin_only=True),
            'dosh': CommandDosh(self.server, admin_only=False),
            'top_kills': CommandTopKills(self.server, admin_only=False),
            'top_dosh': CommandTopDosh(self.server, admin_only=False),
            'top_time': CommandTopTime(self.server, admin_only=False),
            'stats': CommandStats(self.server, admin_only=False),
            'game_time': CommandGameTime(self.server, admin_only=False),
            'server_kills': CommandServerKills(self.server, admin_only=False),
            'server_dosh': CommandServerDosh(self.server, admin_only=False),
            'op': CommandOp(self.server, admin_only=True),
            'deop': CommandOp(self.server, admin_only=True),
            'map': CommandGameMap(self.server, admin_only=False),
            'maps': CommandGameMap(self.server, admin_only=False),
            'lps': CommandLpsTest(self.server, self.chatbot, admin_only=False),
            'player_count': CommandPlayerCount(self.server, admin_only=False),
        }

        return command_map
