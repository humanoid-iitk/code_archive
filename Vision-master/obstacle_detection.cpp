/**
* @file Color_detection_Prototype_Obstacle.cpp
* @brief Finds a single color object and determines on which section of the image it is and where to direct the bot in case.
* @author Priyanshu Gupta
* @status UNDER DEVELOPMENT
* @Known Bugs: The program performs very poorly in situations where there is drastic change of lightening.
*/
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#define WIDTH 1080
#define HEIGHT 1080
//void show_wait_destroy(const char* winname, cv::Mat img);

using namespace std;
using namespace cv;
Mat src; Mat src_gray;
int thresh = 100;
int max_thresh = 255;
Mat imgThresholded;
RotatedRect bounding_rect;
Mat imgOriginal;

void thresh_callback(int, void*);
double segArea(Mat img);
void move_right();
void move_left();
Mat masker(Mat, vector<Point>, float);
vector<Point> contoursConvexHull(vector<vector<Point> > contours);


int main(int argc, char** argv)
{
	//VideoCapture cap(0); //capture the video from web cam
	//VideoCapture cap("2.mp4");//Take a video input
	namedWindow("Mid", CV_WINDOW_NORMAL);
	// Check if camera opened successfully
	if (!cap.isOpened())  // if not success, exit program
	{
		cout << "Cannot open the web cam" << endl;
		return -1;
	}
	
	//////////////////////////////////////////////////////////////////////////
																			//	<-  Comment
	int iLowH = 100;			//Hue Range for Blue color					//	<----------
	int iHighH = 120;														//	<-	This
																			//	<----------
	int iLowS = 0;															//	<-	Section
	int iHighS = 255;														//	<----------	
	int iLowV = 65;// increased to avoid black objects                  	//	<-	while
                   //  from being detected due to lusture					//	<----------
	int iHighV = 150;//Reduced For removing distractions due to lights		//  <-	Callibrating
	//////////////////////////////////////////////////////////////////////////
	
	
	/*
	//Use for Callibrations.

	//For Blue: 90-110


	namedWindow("Control", CV_WINDOW_AUTOSIZE); //create a window called "Control"
												
	int iLowH = 100;
	int iHighH = 120;

	int iLowS = 0;
	int iHighS = 255;

	int iLowV = 0;
	int iHighV = 178;
	
	//Create trackbars in "Control" window
	
	cvCreateTrackbar("LowH", "Control", &iLowH, 179); //Hue (0 - 179)
	cvCreateTrackbar("HighH", "Control", &iHighH, 179);

	cvCreateTrackbar("LowS", "Control", &iLowS, 255); //Saturation (0 - 255)
	cvCreateTrackbar("HighS", "Control", &iHighS, 255);

	cvCreateTrackbar("LowV", "Control", &iLowV, 255);//Value (0 - 255)
	cvCreateTrackbar("HighV", "Control", &iHighV, 255);
	
	*/

	namedWindow("Original", CV_WINDOW_NORMAL);
	createTrackbar(" Canny thresh:", "Original", &thresh, max_thresh, thresh_callback);
	namedWindow("Contours", CV_WINDOW_NORMAL);
	unsigned int i = 0;
	Mat temp1;
	cap.read(temp1);
	cout << "1\n";
	Mat acc(temp1.size(), CV_64FC3, Scalar(0));
	cout << "2\n";
	//VideoWriter video("out4.avi", CV_FOURCC('M', 'J', 'P', 'G'), 10, Size(temp1.size().width, temp1.size().height));
	while (true)
	{
		//free(imgOrig[(i - 1) % 3]);
		Mat temp;
		bool bSuccess = cap.read(temp); // read a new frame from video
		medianBlur(temp, temp, 3);
		temp.convertTo(temp, CV_64FC3);
		acc = acc + temp;
		cout << "3\n";
		if (!bSuccess) //if not success, break loop
		{
			cout << "Cannot read a frame from video stream" << endl;
			break;
		}
		if (i % 4 == 3) {
			
			Mat avg(temp1.size(), CV_8UC3, Scalar(0));
			cout << "4\n";
			Mat t(temp.size(), CV_64FC3, Scalar(0)); // all black, *double* image;
			cout << "5\n";
			acc.convertTo(avg, CV_8UC3, 1.0 / 4);
			cout << "6\n";
			imgOriginal = avg;
			//free(acc);
			acc = t;
			Mat imgHSV;
			//cout << imgOriginal;
			cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV); //Convert the captured frame from BGR to HSV

			inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgThresholded); //Threshold the image

																										  //morphological opening (removes small objects from the foreground)
			erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));

			//morphological closing (removes small holes from the foreground)
			dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
			//cout << imgOriginal;
			medianBlur(imgThresholded, imgThresholded, 3);
			imshow("Thresholded Image", imgThresholded); //show the thresholded image
			thresh_callback(0, 0);
			Point2f rect_points[4]; bounding_rect.points(rect_points);
			for (int j = 0; j < 4; j++)
				line(imgOriginal, rect_points[j], rect_points[(j + 1) % 4], Scalar(0,255,0), 1, 8);
			imshow("Original", imgOriginal); //show the original image
			//video.write(imgOriginal);
			if (waitKey(30) == 27) //wait for 'esc' key press for 30ms. If 'esc' key is pressed, break loop
			{
				cout << "esc key is pressed by user" << endl;
				break;
			}
		}
		i++;
	}
	cap.release();

	return 0;
}
/** @function thresh_callback */
void thresh_callback(int, void*)
{
	Mat canny_output;
	vector<vector<Point> > contours;
	vector<vector<Point> > contourfin;
	vector<Vec4i> hierarchy;
	double largest_area = 0;
	int largest_contour_index = 0;
	/// Detect edges using canny
	long long int cols = imgThresholded.size().width;
	long long int rows = imgThresholded.size().height;
	Canny(imgThresholded, canny_output, thresh, thresh * 2, 3);
	Mat borders(rows + 2, cols + 2, CV_8U);
	for (int i = 0; i < rows; i++) {
		uchar *u = borders.ptr<uchar>(i + 1) + 1;
		uchar *v = canny_output.ptr<uchar>(i);
		for (int j = 0; j < cols; j++, u++, v++) {
			*u = 255 * uchar(*v == 255);
		}
	}
	namedWindow("boundary", CV_WINDOW_KEEPRATIO);
	imshow("boundary", borders);
	/// Find contours
	//findContours(canny_output, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));
	findContours(borders, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_SIMPLE);
	double t = ((borders.size().width)*(borders.size().height));
	for (int i = 0; i < contours.size(); i++) // iterate through each contour. 
	{
		double a = contourArea(contours[i], false); //  Find the area of contour
		if (boundingRect(contours[i]).area() == t) {
			cout << "Holla";
			continue;
		}
		if (a > largest_area) {
			largest_area = a;
			largest_contour_index = i;                //Store the index of largest contour
			bounding_rect = minAreaRect(contours[i]); // Find the bounding rectangle for biggest contour
		}
		if (a > t / 50.000)
			contourfin.push_back(contours[i]);

	}
	cout << largest_area << "\t" << t << "\n";
	/// Draw contours
	//cout << contourfin;
	Mat drawing = Mat::zeros(borders.size(), CV_8UC3);
	Scalar color = Scalar(255, 255, 255);
	if (contourfin.size() != 0) {
		vector<Point> ConvexHullPoints = contoursConvexHull(contourfin);
		
		//polylines(drawing, ConvexHullPoints, true, Scalar(255, 255, 255), 2);
		polylines(imgOriginal, ConvexHullPoints, true, Scalar(0, 0, 255), 2);
		
		drawContours(drawing, contours, largest_contour_index, color, CV_FILLED, 8, hierarchy, 0, Point());
		
		double left, right, mid, leftper, rightper, midper;
		
		left = segArea(drawing(Rect(1, 1, cols / 5, rows)));
		
		mid = segArea(drawing(Rect(cols / 5 + 1, 1, 3 * cols / 5, rows)));
		imshow("mid", drawing(Rect(cols / 5 + 1, 1, 3 * cols / 5, rows)));
		
		right = segArea(drawing(Rect(4 * cols / 5 + 1, 1, cols / 5, rows)));
		
		leftper = left * 100 * 5 / (rows*cols);
		midper = mid * 100 * 5 / (3 * rows*cols);
		rightper = right * 100 * 5 / (rows*cols);
		cout << "Left:\t" << leftper << "\n";
		cout << "Mid:\t" << midper << "\n";
		cout << "Right:\t" << rightper << "\n";
		//cout << drawing;
		double totper = largest_area * 100 / t;
		if (totper > 10) {
			if (midper > 25)
			{
				imgOriginal = masker(imgOriginal, ConvexHullPoints, 0.5);
				if (rightper > leftper)
					move_right();
				else
					move_left();
			}
			else
			{
				imgOriginal = masker(imgOriginal, ConvexHullPoints, 0.10);
			}
		}
		else
		{
			if (rightper > 20 || leftper > 20||midper>5)
			{
				imgOriginal = masker(imgOriginal, ConvexHullPoints, 0.10);
			}
		}
	}
	/// Show in a window
	drawing=drawing(Rect(1, 1, cols, rows));
	imshow("Contours", drawing);
}


double segArea(Mat img)
{
	vector<vector<Point>> contour;
	vector<Vec4i> hierarchy;
	long int cols = img.size().width;
	long int rows = img.size().height;
	cout << "Tat";
	Mat border(rows + 2, cols + 2, CV_8U);
	for (int i = 0; i < rows; i++)
	{
		uchar *u = border.ptr<uchar>(i + 1) + 1;
		uchar *v = img.ptr<uchar>(i);
		for (int j = 0; j < cols; j++, u++, v++)
			*u = 255 * (*v == 255);
	}
	cout << "Tat";
	findContours(border,contour, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_SIMPLE);
	double are = (cols + 2)*(rows + 2),are2=cols*rows,retarea=0;
	int reqInd=-1;
	cout << contour.size();
	for (int i = 0; i < contour.size(); i++)
	{
		double a = contourArea(contour[i]);
		if (are2< a && a < are) {
			cout << "Holla";
			continue;
		}
		else if (a > retarea) {
			reqInd = i;
			retarea = a;
		}
	}
	if (reqInd == -1) {
		return 0;
	}
	return retarea;
}
Mat masker(Mat img, vector<Point> points,float alpha)
{
	Mat newimg = img.clone();
	int side = points.size();
	Point ** pts;
	pts = (Point**)malloc(sizeof(Point*));
	*(pts) = (Point*)malloc(side*sizeof(Point));
	for (int i = 0; i < side; i++)
	{
		pts[0][i] = points.at(i);
	}
	const Point* t[1] = { pts[0] };
	int k[] = { side };
	fillPoly(newimg, t, k, 1, Scalar(0, 0, 255), 8);
	addWeighted(newimg, alpha,img, 1.0-alpha, 0.0, img);
	free(*(pts));
	free(pts);
	return img;
}
void move_right()
{
	cout << "\n\n\n\n\n\n\n\n//////////////////////////////////////////////////////\n\n\n\n\n\n\n\n"<<"Move RIGHT"<< "\n\n\n\n\n\n\n\n//////////////////////////////////////////////////////\n\n\n\n\n\n\n\n";
}
void move_left()
{
	cout << "\n\n\n\n\n\n\n\n//////////////////////////////////////////////////////\n\n\n\n\n\n\n\n" << "Move LEFT" << "\n\n\n\n\n\n\n\n//////////////////////////////////////////////////////\n\n\n\n\n\n\n\n";
}
vector<Point> contoursConvexHull(vector<vector<Point> > contours)
{
	vector<Point> result;
	vector<Point> pts;
	for (size_t i = 0; i< contours.size(); i++)
		for (size_t j = 0; j< contours[i].size(); j++)
			pts.push_back(contours[i][j]);
	convexHull(pts, result);
	return result;
}

