from src.rnn import RNN
from src.training.DataReader import DataReader


def train():
    dr = DataReader(data_dir='data/processed/')

    nn = RNN(
        reader=dr,
        log_dir='logs',
        checkpoint_dir='checkpoints',
        prediction_dir='predictions',
        learning_rates=[.0001, .00005, .00002],
        batch_sizes=[32, 64, 64],
        patiences=[1500, 1000, 500],
        beta1_decays=[.9, .9, .9],
        validation_batch_size=32,
        optimizer='rms',
        num_training_steps=100000,
        warm_start_init_step=0,
        regularization_constant=0.0,
        keep_prob=1.0,
        enable_parameter_averaging=False,
        min_steps_to_checkpoint=2000,
        log_interval=20,
        grad_clip=10,
        lstm_size=400,
        output_mixture_components=20,
        attention_mixture_components=10
    )
    nn.fit()
