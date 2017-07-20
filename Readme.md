
# Usage
One is an idiot, the other's insane.

Git: `https://github.com/TheLampshady/pinky-ponder`


## Install Reqs
2. Install this library for upload
`pip install -t src git+https://github.com/TheLampshady/all_voice.git`


## Create profile
1) Create account in AWS IAM
2) Create profile in CLI: `aws configure --profile <name>`

#Deploy
make deploy FUNCTION=<function> PROFILE=<name>

