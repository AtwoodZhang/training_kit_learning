import _init_paths
from imxcv.config.arguments import get_parser
from imxcv.training.trainer.launch import launch


def main(args):
    pass

if __name__ == "__main__":
    args = get_parser()
    launch(
        main,
    )