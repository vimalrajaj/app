/*
How to Execute:
1. Open this Android project folder in Android Studio.
2. Click the green "Run" arrow in the top toolbar.
*/
package com.example.notifyapp;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn = findViewById(R.id.btnNotify);
        btn.setOnClickListener(v -> {
            NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            NotificationChannel channel = new NotificationChannel("c1", "Alerts", NotificationManager.IMPORTANCE_HIGH);
            nm.createNotificationChannel(channel);
            NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "c1")
                .setSmallIcon(android.R.drawable.ic_dialog_info)
                .setContentTitle("New Alert")
                .setContentText("This is a notification manager demo.");
            nm.notify(1, builder.build());
        });
    }
}