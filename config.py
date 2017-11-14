# preprocessing
BINARY_THRESHOLD = -550
PROCESS_DONE = True

DATASET_PATH = './dataset'
ANNOTATIONS_PATH = './dataset/csv'
# ANNOTATIONS_PATH = '/input/Tianchi/dataset/csv'
PREPROCESS_PATH = './preprocess'
# PREPROCESS_PATH = '/input/Tianchi/preprocess3'

LOG_BASE_PATH = './output/training_logs'
# LOG_BASE_PATH = '/output/training_logs'
MSG_LOG_FILE = '{}/log.log'.format(LOG_BASE_PATH)

# unet model
INPUT_WIDTH, INPUT_HEIGHT, INPUT_DEPTH, INPUT_CHANNEL, OUTPUT_CHANNEL = 64, 64, 64, 1, 1

# try
DIAMETER_SPACING_EXPAND = True
RANDOMIZE_RECORDS= True

# train unet
SEG_LOG_DIR = LOG_BASE_PATH + '/seg-run-{}'
DIAMETER_BUFFER = 2

TRAIN_SEG_EPOCHS = 100000000
TRAIN_SEG_EARLY_STOPPING_PATIENCE = 10
TRAIN_SEG_TRAIN_BATCH_SIZE = 16
TRAIN_SEG_STEPS_PER_EPOCH = 8

TRAIN_SEG_VALID_BATCH_SIZE = 8
TRAIN_SEG_VALID_STEPS = 2

TRAIN_SEG_EVALUATE_FREQ = 4

# DEBUG
DEBUG_PREPROCESS_PLOT = False
DEBUG_SEG_TRY_OVERFIT = False
DEBUG_PART_EVALUATE_CALLBACK = False
# DEBUG_IMAGE_STD = 2000.0
DEBUG_ONLY_TRAIN_SWITCHER_ON = True
DEBUG_ONLY_TRAIN_COVER_RATIO_BIGGER_THAN = 0.1
DEBUG_ONLY_TRAIN_TUMOR_DIAMETER_LARGER_THAN = 12.0
DEBUG_PLOT_WHEN_GET_BATCH = False
DEBUG_MAX_TUMOR_RECORDS_READ = -1

# train classifier
CLASSIFY_LOG_DIR = LOG_BASE_PATH + '/classify-run-{}'
CLASSIFY_POSITIVE_SAMPLE_RATIO = 0.5

TRAIN_CLASSIFY_EPOCHS = 100000000
TRAIN_CLASSIFY_EARLY_STOPPING_PATIENCE = 10
TRAIN_CLASSIFY_TRAIN_BATCH_SIZE = 16
TRAIN_CLASSIFY_VALID_BATCH_SIZE = 8
TRAIN_CLASSIFY_STEPS_PER_EPOCH = 8
TRAIN_CLASSIFY_VALID_STEPS = 1
