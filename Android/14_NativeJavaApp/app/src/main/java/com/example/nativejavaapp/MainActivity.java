/*
How to Execute:
1. Open this Android project folder in Android Studio.
2. Click the green "Run" arrow in the top toolbar.
*/
package com.example.nativejavaapp;

import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(this, "Welcome to Native Java Development!", Toast.LENGTH_LONG).show();
    }
}