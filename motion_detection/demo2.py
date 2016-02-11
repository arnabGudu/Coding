import cv2
import opencv_wrapper as cvw

image = cv2.imread("example.png")

gray = cvw.bgr2gray(image)
thresh = cvw.threshold_otsu(gray, inverse=True)

# dilation
img_dilation = cvw.dilate(thresh, 5)

# Find contours
contours = cvw.find_external_contours(img_dilation)
# Map contours to bounding rectangles, using bounding_rect property
rects = map(lambda c: c.bounding_rect, contours)
# Sort rects by top-left x (rect.x == rect.tl.x)
sorted_rects = sorted(rects, key=lambda r: r.x)

# Distance threshold
dt = 5

# List of final, joined rectangles
final_rects = [sorted_rects[0]]

for rect in sorted_rects[1:]:
    prev_rect = final_rects[-1]

    # Shift rectangle `dt` back, to find out if they overlap
    shifted_rect = cvw.Rect(rect.tl.x - dt, rect.tl.y, rect.width, rect.height)
    intersection = cvw.rect_intersection(prev_rect, shifted_rect)
    if intersection is not None:
        # Join the two rectangles
        min_y = min((prev_rect.tl.y, rect.tl.y))
        max_y = max((prev_rect.bl.y, rect.bl.y))
        max_x = max((prev_rect.br.x, rect.br.x))
        width = max_x - prev_rect.tl.x
        height = max_y - min_y
        new_rect = cvw.Rect(prev_rect.tl.x, min_y, width, height)
        # Add new rectangle to final list, making it the new prev_rect
        # in the next iteration
        final_rects[-1] = new_rect
    else:
        # If no intersection, add the box
        final_rects.append(rect)

for rect in sorted_rects:
    cvw.rectangle(image, rect, cvw.Color.MAGENTA, line_style=cvw.LineStyle.DASHED)

for rect in final_rects:
    cvw.rectangle(image, rect, cvw.Color.GREEN, thickness=2)

cv2.imwrite("result.png", image)

