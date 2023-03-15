if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydra-sjz/Spotify-dl-bot-tg.git /Spotify-dl-bot-tg
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Spotify-dl-bot-tg
fi
cd /Spotify-dl-bot-tg
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 mbot
