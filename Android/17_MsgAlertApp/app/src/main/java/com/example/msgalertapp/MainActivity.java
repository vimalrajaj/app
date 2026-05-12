package com.example.msgalertapp;

import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn = findViewById(R.id.btnAlert);
        btn.setOnClickListener(v -> {
            new AlertDialog.Builder(this)
                .setTitle("SMS Alert")
                .setMessage("Incoming: Your package has arrived!")
                .setPositiveButton("Dismiss", null)
                .show();
        });
    }
}