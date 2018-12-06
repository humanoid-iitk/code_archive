#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace cv;
using namespace std;

/// Global variables

Mat src, src_gray, temp;
Mat dst, detected_edges, mask;

int edgeThresh = 1;
int lowThreshold = 288;
int highThreshold = 500;
int const max_lowThreshold = 500;
int ratio = 3;
int kernel_size = 3;
char* window_name = "Edge Map";
Point2f *center;
float *radius;
int index;
double maxarea;
vector<Point2f> corners;

/**
* @function CannyThreshold
* @brief Trackbar callback - Canny thresholds input with a ratio 1:3
*/
/*
void morphOps(Mat &thresh) {

//create structuring element that will be used to "dilate" and "erode" image.
//the element chosen here is a 3px by 3px rectangle

Mat erodeElement = getStructuringElement(MORPH_RECT, Size(3, 3));
//dilate with larger element so make sure object is nicely visible
Mat dilateElement = getStructuringElement(MORPH_RECT, Size(8, 8));

erode(thresh, thresh, erodeElement);
erode(thresh, thresh, erodeElement);


dilate(thresh, thresh, dilateElement);
dilate(thresh, thresh, dilateElement);



*/


void CannyThreshold(int, void*)
{
	/// Reduce noise with a kernel 3x3
	blur(src_gray, detected_edges, Size(3, 3));
	vector<vector<Point> > contours;
	vector<Vec4i> hierarchy;
	Mat dst1 = Mat::zeros(src.rows, src.cols, CV_8UC3);
	/// Canny detector
	Canny(detected_edges, detected_edges, lowThreshold, highThreshold, kernel_size);
	dilate(detected_edges, mask, getStructuringElement(MORPH_RECT, Size(5, 5)), Point(-1, -1), 3);
	erode(mask, mask, getStructuringElement(MORPH_RECT, Size(5, 5)), Point(-1, -1), 3);
	imshow("mask", mask);
	findContours(mask, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_NONE, Point(0, 0));

	int csize = contours.size();
	if (csize)
	{
		center = new Point2f[csize];
		radius = new float[csize];
		maxarea = contourArea(contours[0]);
		index = 0;

		for (int i = 1; i < csize; i++)
		{
			double area = contourArea(contours[i]);
			if (area > maxarea)
			{
				index = i;
				maxarea = area;
			}
		}
		//vector<RotatedRect> minRect(1);
		Rect boundRect;
		Scalar color = (255, 255, 255);
		//minRect[0] = minAreaRect(Mat(contours[index]));
		boundRect = boundingRect(Mat(contours[index]));	//Point2f rect_points[4]; minRect[0].points(rect_points);
														/* for (int j = 0; j < 4; j++)
														line(temp, rect_points[j], rect_points[(j + 1) % 4], color, 1, 8);*/
														//Point2f vertices[4];
														//minRect.points(vertices);
														//Rect r = boundingRect(contours.at(index));

		rectangle(temp, boundRect.tl(), boundRect.br(), Scalar(172, 255, 135), 1, 8, 0);
		Point2f corner1 = boundRect.br();
		Point2f corner2 = boundRect.tl();
		int a = corner1.x - corner2.x;
		int b = corner1.y - corner2.y;
		line(temp, Point2f((corner2.x + a / 3), corner2.y), Point2f((corner2.x + a / 3), corner1.y), Scalar(0, 255, 0), 1, 8, 0);
		line(temp, Point2f((corner2.x + 2 * a / 3), corner2.y), Point2f((corner2.x + 2 * a / 3), corner1.y), Scalar(0, 255, 0), 1, 8, 0);
		line(temp, Point2f(corner2.x, (corner2.y + b / 3)), Point2f(corner1.x, (corner2.y + b / 3)), Scalar(0, 255, 0), 1, 8, 0);
		line(temp, Point2f(corner2.x, (corner2.y + 2 * b / 3)), Point2f(corner1.x, (corner2.y + 2 * b / 3)), Scalar(0, 255, 0), 1, 8, 0);
		if ((float)a / b < 1.5 && (float)a / b> 0.8)
		{
			Rect r1 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			Rect r2 = Rect(corner2.x + 2 * a / 3, corner2.y, a / 3, b / 3);
			Rect r3 = Rect(corner2.x, corner2.y + 2 * b / 3, a / 3, b / 3);
			Rect r4 = Rect(corner2.x + 2 * a / 3, corner2.y + 2 * b / 3, a / 3, b / 3);

			//if ((r1.x + r1.width < temp.cols) && (r1.y+r1.height<temp.rows))
			Mat R1(temp, r1);
			//Rect r2 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			//if ((r2.x + r2.width < temp.cols) && (r2.y + r2.height<temp.rows))
			Mat R2(temp, r2);
			//Rect r3 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			//if ((r3.x + r3.width < temp.cols) && (r3.y + r3.height<temp.rows))
			Mat R3(temp, r3);
			//Rect r4 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			//if ((r4.x + r4.width < temp.cols) && (r4.y + r4.height<temp.rows))
			Mat R4(temp, r4);
			Rect r5 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			if ((r5.x + r5.width < temp.cols) && (r5.y + r5.height<temp.rows))
				Mat R5(temp, r1);
			Rect r6 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			if ((r6.x + r6.width < temp.cols) && (r6.y + r6.height<temp.rows))
				Mat R6(temp, r1);
			Rect r7 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			if ((r7.x + r7.width < temp.cols) && (r7.y + r7.height<temp.rows))
				Mat R7(temp, r1);
			Rect r8 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			if ((r8.x + r8.width < temp.cols) && (r8.y + r8.height<temp.rows))
				Mat R8(temp, r1);
			Rect r9 = Rect(corner2.x, corner2.y, a / 3, b / 3);
			if ((r9.x + r9.width < temp.cols) && (r9.y + r9.height<temp.rows))
				Mat R9(temp, r1);
			Scalar avgPixelIntensity = mean(R1); int avg1 = (avgPixelIntensity.val[0] + avgPixelIntensity.val[1] + avgPixelIntensity.val[2]) / 3;
			//cout << avgPixelIntensity.val[0] << "   1 \n";
			avgPixelIntensity = mean(R2);	int avg7 = (avgPixelIntensity.val[0] + avgPixelIntensity.val[1] + avgPixelIntensity.val[2]) / 3;
			//cout << avgPixelIntensity1.val[0] << "  7 \n";
			avgPixelIntensity = mean(R3);	int avg9 = (avgPixelIntensity.val[0] + avgPixelIntensity.val[1] + avgPixelIntensity.val[2]) / 3;
			avgPixelIntensity = mean(R4);	int avg3 = (avgPixelIntensity.val[0] + avgPixelIntensity.val[1] + avgPixelIntensity.val[2]) / 3;
			cout << "1 " << avg1 << " 3 " << avg7 << "\n";
			cout << "7 " << avg9 << " 9 " << avg3 << "\n";
		}
		/*int y = corner1.y;
		if (y >= 0 && y < src.cols)
		{
		int x;
		for (x = corner2.x; x <= corner1.x; x++)
		{
		if (x >= 0 && x < src.rows)
		{
		cout << x << ' ' << y << "\n";
		if ((int)detected_edges.at<uchar>(x, y) == 1)
		{
		circle(temp, Point2f(x, y), 1, Scalar(0, 0, 255));
		}
		else if ((int)detected_edges.at<uchar>(x, y) == 0)
		{
		circle(temp, Point2f(x, y), 1, Scalar(255, 0, 0));
		}
		}
		}
		}
		*/
		//rectangle(temp, r.tl(), r.br(), Scalar(172, 255, 135), 1, 8, 0);

		/*int blue;
		int green;
		int red;
		float sum = 0.0;
		float avg;
		int i, j;*/
		/*for (i = corner.x; i >= corner.x - 25; i--)
		{
		for (j = corner.y; j >= corner.y - 25; j--)
		{
		Vec3b intensity = temp.at<Vec3b>(j, i);
		blue = intensity.val[0];
		green = intensity.val[1];
		red = intensity.val[2];
		sum += (blue + green + red) / 3.0;

		}
		}*/
		//avg = sum / 25.0;
		//cout << avg << '\n';
		/*int index; float max = FLT_MIN; int min_index; int min_index2;
		for (index = 0; index < 4; index++)
		{
		Point2f centre;
		centre.x = rect_points[index].x;
		centre.y = rect_points[index].y;
		if (centre.y > max)
		{
		min_index = index;
		max = centre.y;
		}
		}
		max = FLT_MIN;
		for (index = 0; index < 4; index++)
		{
		Point2f centre;
		centre.x = rect_points[index].x;
		centre.y = rect_points[index].y;
		if (centre.y > max && index!=min_index)
		{
		min_index2 = index;
		max = centre.y;
		}
		}
		Point2f corner;
		corner.x = rect_points[min_index].x;
		corner.y = rect_points[min_index].y;
		circle(temp, Point2f(corner.x, corner.y), 10, Scalar(0, 255, 0), 1);
		circle(temp, Point2f(rect_points[min_index2].x, rect_points[min_index2].y), 10, Scalar(0, 0, 255), 1);
		float m1 = 0.5; float m2 = 0.85;
		int dis;
		//for (dis = 0; dis < 100; dis++)
		//{
		//	//dis = 3;
		//	//Point2f point = (corner.x - m1*dis, corner.y - m2*dis);
		//	//Point2f point = (corner.x, corner.y);
		//	circle(temp, Point2f(corner.x - m1*dis, corner.y - m2*dis), 1, Scalar(255, 0, 0), 1);
		//}

		int y; int x;
		x = corner.x;
		y = corner.y;
		int count = 0;
		//cout << src.rows << ' ' << src.cols << '\n';
		for (; y > (corner.y - 80); y--, count++)
		{
		if (y >= 0 && y < src.rows)
		{
		for (; x > rect_points[min_index2].x; x--)
		{
		if (x >= 0 && x < src.cols)
		{
		//int pix = (int)detected_edges.at<uchar>(detected_edges.rows / 2, detected_edges.cols / 2);
		//cout << pix << "  " << x << " " << y << "\n";
		cout << count << ' ' << x << ' ' << y << '\n';
		if ((int)detected_edges.at<uchar>(x, y)==1)
		{
		circle(temp, Point2f(x, y), 1, Scalar(0, 0, 255));
		}
		else if ((int)detected_edges.at<uchar>(x, y) == 0)
		{
		circle(temp, Point2f(x, y), 1, Scalar(255, 0, 0));
		}
		}
		}
		}
		}*/
		/*if (avg >= 5000)
		{
		cout << "Left Arrow" << '\n';
		}
		else if (avg <= 2000)
		{
		cout << "Right Arrow" << '\n';
		}
		else
		{
		cout << "No arrow detected" << '\n';
		}*/


		//Vec3b bgr = temp.at<Vec3b>(r.tl().x, r.br().y);
		//cout << bgr.val[0] << "  " << bgr.val[1] << "  " << bgr.val[2] << "\n";
		/*Vec3b intensity = temp.at<Vec3b>(r.br().y, r.br().x);
		int blue = intensity.val[0];
		int green = intensity.val[1];
		int red = intensity.val[2];
		cout << intensity.val[0] << "  " << intensity.val[1] << "  " << intensity.val[2] << "\n";*/
	}

	imshow("temp", temp);
	imshow("canny", detected_edges);
	imshow("contour", dst1);
	/// Using Canny's output as a mask, we display our result
	dst = Scalar::all(0);
	src.copyTo(dst, detected_edges);
	imshow(window_name, dst);

}


/** @function main */
int main(int argc, char** argv)
{
	VideoCapture cam(0);
	while (waitKey(10) != 'q') {
		/// Load an image

		cam.read(src);
		temp = src;
		/*if (!src.data)
		{
		return -1;
		}*/

		/// Create a matrix of the same type and size as src (for dst)
		dst.create(src.size(), src.type());

		/// Convert the image to grayscale
		cvtColor(src, src_gray, CV_BGR2GRAY);

		/// Create a window
		namedWindow(window_name, CV_WINDOW_AUTOSIZE);

		/// Create a Trackbar for user to enter threshold
		createTrackbar("Min Threshold:", window_name, &lowThreshold, max_lowThreshold, CannyThreshold);
		createTrackbar("Max Threshold:", window_name, &highThreshold, max_lowThreshold, CannyThreshold);

		/// Show the image
		CannyThreshold(0, 0);

		/// Wait until user exit program by pressing a key
	}

	return 0;
}
