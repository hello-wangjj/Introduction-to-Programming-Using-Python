from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score, roc_curve, auc, roc_auc_score, \
    accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from scipy import interp
import numpy as np

__author__ = 'wangj'
__date__ = '2018/01/15 19:45'


def main():
    pass


if __name__ == '__main__':
    df = datasets.load_breast_cancer()
    x = df.data
    y = df.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    pipe_svc = Pipeline(
        [('sc1', StandardScaler()), ('clf', SVC(random_state=1, C=0.1, kernel='linear', probability=True))])
    pipe_svc.fit(x_train, y_train)
    y_pred = pipe_svc.predict(x_test)
    conf_mat = confusion_matrix(y_true=y_test, y_pred=y_pred)
    print(conf_mat)
    plt.figure(1)
    fig, ax = plt.subplots(figsize=(2.5, 2.5))
    ax.matshow(conf_mat, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(conf_mat.shape[0]):
        for j in range(conf_mat.shape[1]):
            ax.text(x=j, y=i, s=conf_mat[i, j], va='center', ha='center')
    plt.xlabel('predict label')
    plt.ylabel('real label')
    plt.show()
    print('Precision {0:.3f}'.format(precision_score(y_true=y_test, y_pred=y_pred)))
    print('Recall {0:.3f}'.format(recall_score(y_true=y_test, y_pred=y_pred)))
    print('f1 {0:.3f}'.format(f1_score(y_true=y_test, y_pred=y_pred)))
    x_train_2 = x_train[:, [4, 14]]
    cv = StratifiedKFold(n_splits=3, random_state=1)
    fig = plt.figure(num=2, figsize=(7, 5))
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)
    for k, (train, test) in enumerate(cv.split(x_train, y_train)):
        probas_ = pipe_svc.fit(x_train_2[train], y_train[train]).predict_proba(x_train_2[test])
        fpr, tpr, thresholds = roc_curve(y_train[test], probas_[:, 1], pos_label=1)
        tprs.append(interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, lw=1, label='Roc fold {0:d} (area = {1:0.2f} )'.format(k + 1, roc_auc))
    plt.plot([0, 1], [0, 1], linestyle='--', color=(0.6, 0.6, 0.6), label='random guessing')
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k--', color=(0.6, 0.6, 0.6),
             label='mean roc (area = {0:0.2f} )'.format(mean_auc), lw=2)
    plt.plot([0, 0, 1], [0, 1, 1], linestyle=':', color='black', lw=2, label='perfect performance')
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('false positive rate')
    plt.ylabel('true positive rate')
    plt.legend(loc='best')
    plt.show()

    # 仅计算 roc auc
    pipe_svc = pipe_svc.fit(x_train_2, y_train)
    y_pred_2 = pipe_svc.predict(x_test[:, [4, 14]])
    print('ROC accuracy: {0:.3f}'.format(accuracy_score(y_true=y_test, y_pred=y_pred_2)))
