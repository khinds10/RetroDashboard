package com.kevinhinds.dashboardphone;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.support.v4.content.LocalBroadcastManager;
import android.telephony.PhoneStateListener;
import android.telephony.TelephonyManager;

/**
 * incoming call listener http post information about it
 */
public class ServiceReceiver extends BroadcastReceiver {

	@Override
	public void onReceive(final Context context, Intent intent) {
		TelephonyManager telephony = (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
		telephony.listen(new PhoneStateListener() {
			@Override
			public void onCallStateChanged(int state, String incomingNumber) {
				super.onCallStateChanged(state, incomingNumber);
				System.out.println("incomingNumber : " + incomingNumber);
				Intent msgrcv = new Intent("Msg");
				msgrcv.putExtra("package", "");
				msgrcv.putExtra("ticker", incomingNumber);
				msgrcv.putExtra("title", incomingNumber);
				msgrcv.putExtra("text", "");
				
				// publish over to Settings.remoteDashboardHost
				PublishService ps = new PublishService();
				ps.pushNotification("Call:", incomingNumber, incomingNumber, "");
				LocalBroadcastManager.getInstance(context).sendBroadcast(msgrcv);
			}
		}, PhoneStateListener.LISTEN_CALL_STATE);
	}
}