import argparse


def get_parser():
    # 1. 创建ArgumentParser对象，解析命令行；
    parser = argparse.ArgumentParser(description="Training Pipeline")  
    # 2. 添加参数；
    parser.add_argument("-c", "--config-file", default="", type=str, help="configs file")
    parser.add_argument("--gpu-id", nargs="+", default=[0], type=int, help='specify your GPU ids') # nargs 表示命令行需要使用的参数数目必须 > 0.
    parser.add_argument("--distributed", action='store_true', default=False, help='use distributed training')  # 当参数在命令行中出现时，使用的动作（action)基本类型，表示该选项要执行的操作；
    parser.add_argument("--resume", default="", type=str, help="model weights to resume training")
    parser.add_argument("--test", default="", type=str, help="model weights to be tested on a dataset")
    parser.add_argument("-w", "--weight", type=str, default="", help="trained model weight")
    parser.add_argument("-i", "--input-shape", type=str, default="(224, 224)", help="model input size of (width, height)")
    parser.add_argument("-o", "--onnx-output", type=str, default="", help="onnx model saved path")
    parser.add_argument("--verbose", default=False, help="show intermediate info")
    parser.add_argument("opts", default=None, nargs=argparse.REMAINDER, help="Modify config options by adding 'KEY VALUE' pairs at the end of the command. ")  
    # 当 nargs 设置为 argparse.REMAINDER 时，意味着该选项将消耗所有剩余的命令行参数，无论它们是否以破折号（"-"）开头。
    return parser.parse_args()