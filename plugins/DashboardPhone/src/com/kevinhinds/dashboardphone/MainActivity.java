package com.kevinhinds.dashboardphone;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.support.v4.content.LocalBroadcastManager;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ListView;

import java.util.ArrayList;

/**
 * dashboard phone main activity
 * @author khinds
 */
public class MainActivity extends Activity {

	ListView list;
	CustomListAdapter adapter;
	ArrayList<Model> modelList;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		modelList = new ArrayList<Model>();
		adapter = new CustomListAdapter(getApplicationContext(), modelList);
		list = (ListView) findViewById(R.id.list);
		list.setAdapter(adapter);
		LocalBroadcastManager.getInstance(this).registerReceiver(onNotice, new IntentFilter("Msg"));
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.menu_main, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch (item.getItemId()) {
		case R.id.action_settings:
			Intent intent = new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS");
			startActivity(intent);
			return true;
		default:
			return super.onOptionsItemSelected(item);
		}
	}

	/**
	 * register a broadcast receiver to receive incoming phone notifications
	 */
	private BroadcastReceiver onNotice = new BroadcastReceiver() {

		@Override
		public void onReceive(Context context, Intent intent) {
			String title = intent.getStringExtra("title");
			String text = intent.getStringExtra("text");
			try {
				byte[] byteArray = intent.getByteArrayExtra("icon");
				Bitmap bmp = null;
				if (byteArray != null) {
					bmp = BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
				}
				Model model = new Model();
				model.setName(title + " " + text);
				model.setImage(bmp);

				if (modelList != null) {
					modelList.add(model);
					adapter.notifyDataSetChanged();
				} else {
					modelList = new ArrayList<Model>();
					modelList.add(model);
					adapter = new CustomListAdapter(getApplicationContext(), modelList);
					list = (ListView) findViewById(R.id.list);
					list.setAdapter(adapter);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	};
}