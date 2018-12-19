# Genre-specific-MuseGAN
All the operations below assume the working directory is the musegan root directory.
## Prerequisites

### Install dependencies
- Using pip

  ```sh
  # Install the dependencies
  pip install -r requirements.txt
  ```
  
  If there's anything wrong, here is the solution for my environment:   
  - Install the latest Miniconda
  - Downgrade the python to python3.5 by 
  ```sh
  conda install python=3.5
  ```
  - Try it again!
  
  If there's still some packages missing during training, just pip install or conda install the reported one.
  
### Prepare training data
```sh
# Store the training data to shared memory
./scripts/process_data.sh
```

## Train a new model
1. Run the following command to set up a new experiment with default settings.

   ```sh
   # Set up a new experiment
   ./scripts/setup_exp.sh "./exp/my_experiment/" "Some notes on my experiment"
   ```

2. (Optional) Modify the configuration and model parameter files for experimental settings by modifying config.yaml and params.yaml in ./exp/my_experiment.

3. Train the model:

     ```sh
     # Train the model
     ./scripts/run_train.sh "./exp/my_experiment/"
     ```

## Generate Music
```sh
./scripts/run_inference.sh "./exp/my_experiment/" "the_genre_you_want_to_generate(jazz, rock or disco)"
# for example
# ./scripts/run_inference.sh "./exp/1/" "jazz"
```
