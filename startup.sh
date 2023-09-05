#!/bin/bash

# Only the first time:
if [ ! -f initialized ]
then
	# The PatchCore repo:
	git clone https://github.com/amazon-science/patchcore-inspection.git

	# All done:
	touch initialized
fi

# Starting a notebook server:
export PYTHONPATH="$PWD/patchcore-inspection"
pipenv run jupyter notebook --no-browser --allow-root -y --ip 0.0.0.0 --port 8888
