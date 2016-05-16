package com.kevinhinds.dashboardphone;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.protocol.HTTP;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

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

		// build JSON string to HTTP Post to remote server
		DefaultHttpClient httpclient = new DefaultHttpClient();		
		HttpPost httppostreq = new HttpPost(Settings.remoteDashboardHost);
		StringEntity se;
		String responseText = null;
		JSONObject jsonObjSend = new JSONObject();
		JSONObject jsonObjRecieved = new JSONObject();
		try {
			jsonObjSend.put("Package", pack);
			jsonObjSend.put("Ticker", ticker);
			jsonObjSend.put("Title", title);
			jsonObjSend.put("Text", text);
			se = new StringEntity(jsonObjSend.toString());
			se.setContentType("application/json;charset=UTF-8");
			se.setContentEncoding(new BasicHeader(HTTP.CONTENT_TYPE, "application/json;charset=UTF-8"));
			httppostreq.setEntity(se);
			HttpResponse httpresponse = httpclient.execute(httppostreq);
			responseText = EntityUtils.toString(httpresponse.getEntity());
			jsonObjRecieved = new JSONObject(responseText);
		} catch (Exception e1) {
		}
		return jsonObjRecieved;
	}
}