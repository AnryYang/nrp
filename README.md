## Layout
1. data
2. algos
3. eval
4. embds

## Input
See an example in data/wiki/
1. attrs.txt
2. edgelist.txt
3. labels.txt

## Output
In embds/wiki/


## Preprocessing
1. Split training, testing and negative edge sets for link prediction
```sh
$ cd eval/
$ python splitTrainTest.py --action split --data wiki --ratio=0.3
$ python splitTrainTest.py --action select --data wiki --ratio=0.3
```
2. Generate node pairs for graph reconstruction
```sh
$ cd eval/
$ python gen_nodepairs.py --data wiki --ratio=0.01
```

## Algorithm
See readme.md in algos/nrp/

## Evaluation
```sh
$ cd eval/
$ python eval_linkpred.py --algo nrp --data wiki --d 128
$ python graphreconstruct_util.py --algo nrp --data wiki --d 128
```

## Citation
```
@article{yang2020homogeneous,
  title={Homogeneous network embedding for massive graphs via reweighted personalized PageRank},
  author={Yang, Renchi and Shi, Jieming and Xiao, Xiaokui and Yang, Yin and Bhowmick, Sourav S},
  journal={Proceedings of the VLDB Endowment},
  volume={13},
  number={5},
  pages={670--683},
  year={2020},
  publisher={VLDB Endowment}
}
```