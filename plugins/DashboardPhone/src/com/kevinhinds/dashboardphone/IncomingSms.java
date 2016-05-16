package com.kevinhinds.dashboardphone;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.content.LocalBroadcastManager;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import android.util.Log;

/**
 * incoming sms handler http post information about it
 */
public class IncomingSms extends BroadcastReceiver {

	// get the object of SmsManager
	final SmsManager sms = SmsManager.getDefault();

	public void onReceive(Context context, Intent intent) {

		// retrieves a map of extended data from the intent.
		final Bundle bundle = intent.getExtras();
		try {
			if (bundle != null) {
				final Object[] pdusObj = (Object[]) bundle.get("pdus");
				for (int i = 0; i < pdusObj.length; i++) {

					SmsMessage currentMessage = SmsMessage.createFromPdu((byte[]) pdusObj[i]);
					String phoneNumber = currentMessage.getDisplayOriginatingAddress();

					String senderNum = phoneNumber;
					String message = currentMessage.getDisplayMessageBody();

					Log.i("SmsReceiver", "senderNum: " + senderNum + "; message: " + message);

					Intent msgrcv = new Intent("Msg");
					msgrcv.putExtra("package", "");
					msgrcv.putExtra("ticker", senderNum);
					msgrcv.putExtra("title", senderNum);
					msgrcv.putExtra("text", message);

					// publish over to your server with the Settings.remoteDashboardHost RetroDashboard listener installed 
					PublishService ps = new PublishService();
					ps.pushNotification("SMS:", senderNum, senderNum, message);

					LocalBroadcastManager.getInstance(context).sendBroadcast(msgrcv);
				}
			}
		} catch (Exception e) {
			Log.e("SmsReceiver", "Exception smsReceiver" + e);
		}
	}
}