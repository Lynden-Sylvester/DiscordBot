import os
import socket

class Bot:
  def __init__(self):
    self.irc_server = "irc.twitch.tv"
    self.irc_port = 6667
    self.oauth_token = os.environ.get("TWITCH_OAUTH_TOKEN")
    self.username = os.environ.get("BOT_NICK")
    self.channels = [os.environ.get("CHANNEL")]

bot = commands.Bot(
  irc_token = os.environ.get("TMI_TOKEN"),
  client_id = os.environ.get("TWITCH_CLIENT_ID"),
  nick = os.environ.get("BOT_NICK"),
  prefix = os.environ.get("BOT_PREFIX"),
  initial_channel = os.environ.get("CHANNEL")
)

print("Hello")