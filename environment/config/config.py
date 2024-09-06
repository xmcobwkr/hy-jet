from importlib.resources import Resource

from math import log

import numpy as np
import torch

SEED = 3407
CUDA_VISIBLE_DEVICES = 0
np.random.seed(SEED)
torch.manual_seed(SEED)
# NUM_OFFLOADING_COUNT = 10

LOG = True

EXAMPLE_PATH = "data/hypergraph_example.json"

DATASET_PATH = "./data/dag_data"

NUM_HG_TASKS = 20
NUM_HG_EDGES = 0
NUM_HG = 1
MAX_DATA_SIZE = 50 * 1024 * 1024 * 8

USE_GRAPH_STATE = False
USE_HG_EDGE = [True, True, True, True]
HG_EDGE_NUM = [NUM_HG_TASKS + 10, NUM_HG_TASKS, NUM_HG_TASKS // 4, NUM_HG_TASKS // 4]
for k, v in zip(USE_HG_EDGE, HG_EDGE_NUM):
    NUM_HG_EDGES += v if k else 0
GRAPH_STATE_TYPE = "HG"
EXP = None

EMBED_SIZE = 64
BATCH_SIZE = 16
EPOCH = 300
NUM_TRAIN_HG = 5
NUM_TEST_HG = 5
STEP_PER_EPOCH=NUM_HG * NUM_HG_TASKS * NUM_TRAIN_HG
# STEP_PER_EPOCH=1
EPISODE_PER_COLLECT = BATCH_SIZE
REPEAT_PER_COLLECT = 1
EPISODE_PER_TEST = BATCH_SIZE
PATIENCE = 200

GNN_TYPE = None


BASE_POLICY = None

NORMAL_NET = ["Seq2Seq"]

PARTITIONING_CONFIG = "km1_rKaHyPar_sea20.ini"

SELF_ATTENTION = False

USE_CACHE = False

USE_HEFT = False

NORMAL_NET_STR = '-'.join(NORMAL_NET)
EXPERIMENT_SUFFIX = f"-{NORMAL_NET_STR}-{np.where(np.array(USE_HG_EDGE))[0]}-task{NUM_HG * NUM_HG_TASKS}-edge{NUM_HG_EDGES * NUM_HG}-{PARTITIONING_CONFIG}"

GAMMA = 0.95
MAX_GRAD_NORM = 0.4
GAE_LAMBDA = 0.95
REW_NORM = 1
DUAL_CLIP = None
VALUE_CLIP = 1
NORM_ADV = 1
VF_COEF = 0.25
ENT_COEF = 0
EPS_CLIP = 0.2
DETERMINISTIC_EVAL = True
BUFFER_SIZE = 20000
TASK_COMPLEXITIES = {"O(1)": lambda n: 1, "O(n)": lambda n: n,
                     "O(nlogn)": lambda n: n * log(n), "O(nlogn^2)": lambda n: n * log(n)**2,
                     "O(n^2)": lambda n: n**2, "O(n^2logn)": lambda n: n**2 * log(n),
                     "O(n^3)": lambda n: n**3, "O(2^n)": lambda n: 2**n}
TASK_COMPLEXITIES_RATE = [0, 0.3, 0.7, 0, 0, 0, 0, 0]
TASK_CONSTANTS = list(range(1, 11))
TASK_CONSTANTS_RATE = [0.1] * 10

NUM_RESOURCE_CLUSTER = 4
NUM_EDGE_CLUSTER = (NUM_HG + 1) // 2

UPLOAD_BANDWIDTHS = [10 * 1024 * 1024, 20 * 1024 * 1024, 500 * 1024 * 1024, 1024 * 1024 * 1024]

DOWNLOAD_BANDWIDTHS = [100 * 1024 * 1024, 50 * 1024 * 1024, 500 * 1024 * 1024, 1024 * 1024 * 1024]

LOAD_ENERGY = [10, 20, 30, 40]

BANDWIDTHS_RATE = [0.35, 0.639, 0.01, 0.001]

BASE_INT = 32

CPU_FREQUENCIES = [2.0 * 10**9, 3 * 10**9, 3.6 * 10**9, 3.7 * 10**9, 4.5 * 10**9, 4.9 * 10**9]

LOCAL_CPU_FREQUENCY = 1.0 * 10 ** 9

LOCAL_ENERGY_COEFFICIENT = 20

ENERGY_COEFFICIENT = [20, 30, 40, 40, 40, 50]

MS2S = 1000

MAX_INPUT_N = MAX_DATA_SIZE / BASE_INT
MAX_EXEC_TIME = MAX_INPUT_N * MAX_INPUT_N * BASE_INT / min(CPU_FREQUENCIES) / MS2S
MAX_TIME = NUM_HG * NUM_HG_TASKS * (MAX_DATA_SIZE / min(UPLOAD_BANDWIDTHS) + MAX_DATA_SIZE / min(DOWNLOAD_BANDWIDTHS) + MAX_EXEC_TIME) / MS2S
MAX_ENERGY = NUM_HG * NUM_HG_TASKS * MAX_EXEC_TIME / MS2S * max(ENERGY_COEFFICIENT)

TIME_BENCHMARK_DIMENSION_WEIGHT = -10

ENERGY_BENCHMARK_DIMENSION_WEIGHT = -1

REWARD_WEIGHT = {
    "time": .5,
    "energy": .5
}
CRITICAL_PATH_WEIGHT = .5



