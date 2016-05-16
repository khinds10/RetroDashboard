package com.kevinhinds.dashboardphone;

import android.graphics.Bitmap;

/**
 * model to encapsulate notifications 
 * 	to present as a list on the main application view 
 */
public class Model {
	String name;
	Bitmap imaBitmap;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Bitmap getImage() {
		return imaBitmap;
	}

	public void setImage(Bitmap imaBitmap) {
		this.imaBitmap = imaBitmap;
	}
}