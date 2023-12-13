# Models

This folder contains notebooks for our work modeling the price.

## Files

- `dt.ipynb`: Notebook for our Decision Tree model.

- `knn.ipynb`: Notebook for our KNN model.

- `rf.ipynb`: Notebook for our Random Forest (ensemble) model.

## KNN Regression

Notes on the KNN model.

### Notable Changes

After updating the data pre-processing, I re-ran the KNN model:

* Training samples went from 7009 -> 7001.

#### R2 results for KNN with older data:
| K | Test R2 | Train R2 |
| --- | --- | --- |
| 5 | 0.0008040154979879199 | 0.17977696608285532 |
| 6 | 0.1411911947661597 | 0.16643213159807746 |
| 7 | 0.12425772455590434 | 0.15282217668851883 |
| 8 | 0.1108127957041688 | 0.13256402729049965 |

#### Results with cleaner data:
| K | Test R2 | Train R2 | 
| --- | --- | --- |
| 5 | 0.8644741640601704 | 0.6606602118046967 |
| 6 | 0.8713803040996428 | 0.6397757844687746 |
| 7 | 0.8692824717948242 | 0.6115449665102355 |
| 8 | 0.8687516010976353 | 0.589063313392763 |

| K | Test Mean AE | Train Mean AE | 
| --- | --- | --- |
| 5 | 0.1325378493805926 | 0.12301667814067577 |
| 6 | 0.13597014873452304 | 0.13214068256539496 |
| 7 | 0.14075470223374853 | 0.14068042164250563 |
| 8 | 0.14408334570586023 | 0.14723194803361775 |

| K | Test Mean SE | Train Mean SE | 
| --- | --- | --- |
| 5 | 0.07578135435519463 | 0.3767237798603035 |
| 6 | 0.07191967999673347 | 0.39990897853107743 |
| 7 | 0.07309271517609083 | 0.4312498964542299 |
| 8 | 0.07338955968652294 | 0.45620828222138304 |

| K | Test Median AE | Train Median AE | 
| --- | --- | --- |
| 5 | 0.0485564738721998 | 0.032741330733140256 |
| 6 | 0.05344826213077272 | 0.04039029712779443 |
| 7 | 0.05856244171786311 | 0.0462752752079002 |
| 8 | 0.06173719651683206 | 0.0483136723468999 |
