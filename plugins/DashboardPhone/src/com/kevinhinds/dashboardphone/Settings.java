package com.kevinhinds.dashboardphone;

/**
 * specific settings for your dashboard phone installation here
 * 
 * @author khinds
 */
public class Settings {

	// host with the PHP server script installed for the RetroDashboard
	public static String remoteDashboardHost = "YOUR-SERVER-HERE.com";

	// create a list of notifications (by title) your phone always produces but don't need to broadcast
	public static String[] ignoredNotifications = new String[] { "Privacy Guard active", "Change keyboard", "Select keyboard", "Calls will be made" };
}