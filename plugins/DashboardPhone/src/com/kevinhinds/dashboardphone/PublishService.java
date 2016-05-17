package com.kevinhinds.dashboardphone;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.protocol.HTTP;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

import android.os.StrictMode;
import android.util.Log;

/**
 * publish phone notifications to Settings.remoteDashboardHost
 * 
 * @author khinds
 */
public class PublishService {

	/**
	 * push phone notification over to the dashboard receiver on Settings.remoteDashboardHost
	 * 
	 * @param pack
	 * @param ticker
	 * @param title
	 * @param text
	 */
	public JSONObject pushNotification(String pack, String ticker, String title, String text) {

		// let's keep it simple, no additional threading for these small HTTP POSTs
		StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
		StrictMode.setThreadPolicy(policy);
		
		// for the list of ignored applications return null and not push to remote server
		for (String ignoredMessage : Settings.ignoredNotifications) {
			if (title.contains(ignoredMessage)) {
				return null;
			}
		}

		// build JSON string to HTTP Post to remote server
		DefaultHttpClient httpclient = new DefaultHttpClient();
		HttpPost httppostreq = new HttpPost("http://" + Settings.remoteDashboardHost + "/message/set");
		StringEntity se;
		String responseText = null;
		JSONObject jsonObjRecieved = new JSONObject();
		try {
			se = new StringEntity(title + " - " +  text);
			se.setContentType("application/json;charset=UTF-8");
			se.setContentEncoding(new BasicHeader(HTTP.CONTENT_TYPE, "application/json;charset=UTF-8"));
			httppostreq.setEntity(se);
			HttpResponse httpresponse = httpclient.execute(httppostreq);
			responseText = EntityUtils.toString(httpresponse.getEntity());
			jsonObjRecieved = new JSONObject(responseText);
		} catch (Exception e) {
			Log.d("Could not HTTP POST", e.getMessage());
		}
		return jsonObjRecieved;
	}
}