
# model 1
Y_pred_cls= {
        'model_name': 'Model 1',
        'model_accuracy' : 0.9986482216214319,
        'recall_score': 0.9489795918367347,
        'precision_score': 0.5636363636363636,
        'f-score': 0.7072243346007604
    }

def m_accuracy(score):
    return int(score * 56868.874114441416)

def r_score(score):
        return int(score * 75.87096774193547)

def p_score(score):
    return int(score * 8.870967741935484)

def f_score(score):
    return int(score * 131.5)

# model 2
Y_mod2_cls = {
        'model_name': 'Model 2',
        'model_accuracy': 0.9992099996488887,
        'loss_value': 0.008827306184946626,
        'recall_score': 0.9693877551020408,
        'precision_score': 0.6934306569343066,
        'f-score': 0.8085106382978723,
    }


def m2_accuracy(score):
    return int(score * 56866.92489063022)

def r2_score(score):
        return int(score * 43.32631578947369)

def p2_score(score):
    return int(score * 4.326315789473684)

def f2_score(score):
    return int(score * 117.50000000000001)



print(m2_accuracy(Y_pred_cls['model_accuracy']))
print(r2_score(Y_pred_cls['recall_score']))
print(p2_score(Y_pred_cls['precision_score']))
print(f2_score(Y_pred_cls['f-score']))

