from happysadsongs.data import clean
from statistics import mode

def get_split(lyric):
    """Split complete song lyric into 20-word segments, with 10 word overlaps.
    Returns list of segments as strings."""
    l_total = []
    l_part = []
    if len(lyric.split()) // 20 > 0:
        n = len(lyric.split()) // 20
    else:
        n = 1
    for w in range(n):
        if w == 0:
            l_part = lyric.split()[:30]
            l_total.append(" ".join(l_part))
        else:
            l_part = lyric.split()[w * 20:w * 20 + 30]
            l_total.append(" ".join(l_part))
    return l_total

def predict_parts(model, lyric):
    """Cleans input lyric with standard preprocess stepps. Then runs model
    prediction on each 20-word segment generated by get_split function and
    finally returns mode of preds.
    Note: returns 1 (highest value) if equal number of 0 and 1 predictions"""
    lyric_parts = get_split(clean(lyric))
    preds = model.predict(lyric_parts)[0]
    try:
        return int(mode(preds))
    except:
        return 1