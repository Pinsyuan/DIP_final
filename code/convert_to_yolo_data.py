import json
from collections import defaultdict
import csv

with open("../EasyCV/data/coco/annotations/instances_train2017.json") as f:
	train_annotations = json.load(f)

with open("../EasyCV/data/coco/annotations/instances_val2017.json") as f:
	valid_annotations = json.load(f)

train_image_labels = defaultdict(list)
valid_image_labels = defaultdict(list)
train_id_to_image_info = {}
valid_id_to_image_info = {}

for i in train_annotations['images']:
	train_id_to_image_info[i['id']] = {
		"file_name": i['file_name'],
		"height": i['height'],
		'width': i['width']
	}

for i in valid_annotations['images']:
	valid_id_to_image_info[i['id']] = {
		"file_name": i['file_name'],
		"height": i['height'],
		'width': i['width']
	}

for a in train_annotations['annotations']:
	train_image_labels[a['image_id']].append([a['category_id'], a['bbox'][0] / train_id_to_image_info[a['image_id']]['width'], a['bbox'][1] / train_id_to_image_info[a['image_id']]['height'], a['bbox'][2] / train_id_to_image_info[a['image_id']]['width'], a['bbox'][3] / train_id_to_image_info[a['image_id']]['height']])

for a in valid_annotations['annotations']:
	valid_image_labels[a['image_id']].append([a['category_id'], a['bbox'][0] / valid_id_to_image_info[a['image_id']]['width'], a['bbox'][1] / valid_id_to_image_info[a['image_id']]['height'], a['bbox'][2] / valid_id_to_image_info[a['image_id']]['width'], a['bbox'][3] / valid_id_to_image_info[a['image_id']]['height']])

for image_id in train_id_to_image_info:
	with open('train/labels/{}'.format(train_id_to_image_info[image_id]['file_name'].replace('jpg', 'txt')), 'w', newline = '') as f:
		writer = csv.writer(f, delimiter = ' ')

		for row in train_image_labels[image_id]:
			writer.writerow(row)

for image_id in valid_id_to_image_info:
	with open('valid/labels/{}'.format(valid_id_to_image_info[image_id]['file_name'].replace('jpg', 'txt')), 'w', newline = '') as f:
		writer = csv.writer(f, delimiter = ' ')

		for row in valid_image_labels[image_id]:
			writer.writerow(row)


