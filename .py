def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesi"""
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

# 2D uzaydaki noktaları tanımlama
points = [(1, 2), (4, 6), (7, 8), (2, 1), (9, 10)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print("En küçük Öklid mesafesi:", min_distance)
