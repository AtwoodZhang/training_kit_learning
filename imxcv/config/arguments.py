import argparse


def get_parser():
    # 1. 创建ArgumentParser对象，解析命令行；
    parser = argparse.ArgumentParser(description="Training Pipeline")  
    # 2. 添加参数；
    parser.add_argument("--gpu-id", nargs="+", default=[0], type=int, help='specify your GPU ids') # nargs 表示命令行需要使用的参数数目必须 > 0.
    parser.add_argument("--distributed", action='store_true', default=False, help='use distributed training')  # 当参数在命令行中出现时，使用的动作（action)基本类型，表示该选项要执行的操作；
    