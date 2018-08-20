from simple_plot import add_button, add_click, get_a, redraw, start
import random

points = []
labels = []
means = []

def distance(p1, p2):
    return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])

def vplus(p1, p2):
    return [p1[0]+p2[0], p1[1]+p2[1]]

def ktimesv(k, p):
    return [k*p[0], k*p[1]]

def train(points, labels):
    k = 0
    for i in range(0, len(points)):
        if labels[i]>k:
            k = labels[i]+1
    means = []
    for j in range(0, k):
        mean = [0, 0]
        count = 0
        for i in range(0, len(points)):
            if labels[i]==j:
                mean = vplus(mean, points[i])
                count = count+1
        mean = ktimesv(1.0/count, mean)
        means.append(mean)
    return means

def classify(point, means):
    best_distance = float("inf")
    best_label = -1
    for j in range(0, len(means)):
        d = distance(point, means[j])
        if d<best_distance:
            best_distance = d
            best_label = j
    return best_label

def redisplay():
    get_a().clear()
    for i in range(0, len(points)):
        if labels[i]==0:
            get_a().plot([points[i][0]], [points[i][1]], "r+")
        elif labels[i]==1:
            get_a().plot([points[i][0]], [points[i][1]], "b+")
    if len(means)==2:
        get_a().plot([means[0][0]], [means[0][1]], "ro")
        get_a().plot([means[1][0]], [means[1][1]], "bo")
    redraw()

def clear_command():
    global points, labels
    points = []
    labels = []
    get_a().clear()
    redraw()

def random_labels_command():
    global labels
    for i in range(0, len(points)):
        labels[i] = random.randint(0, 1)
    redisplay()

def train_command():
    global means
    means = train(points, labels)
    redisplay()

def reclassify_all_command():
    global labels
    for i in range(0, len(points)):
        labels[i] = classify(points[i], means)
    redisplay()

def click(x, y):
    points.append([x, y])
    labels.append(-1)
    get_a().plot([x], [y], "g+")
    redraw()

add_button("Clear", clear_command)
add_button("Random labels", random_labels_command)
add_button("Train", train_command)
add_button("Reclassify all", reclassify_all_command)
add_button("Exit", exit)
add_click(click)
start()