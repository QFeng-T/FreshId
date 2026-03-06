package com.tianhu.app

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class ResultActivity : AppCompatActivity() {

    private lateinit var backButton: Button
    private lateinit var shareButton: Button
    private lateinit var favoriteButton: Button
    private lateinit var recognizeAgainButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        // 初始化视图
        backButton = findViewById(R.id.backButton)
        shareButton = findViewById(R.id.shareButton)
        favoriteButton = findViewById(R.id.favoriteButton)
        recognizeAgainButton = findViewById(R.id.recognizeAgainButton)

        // 设置点击事件
        backButton.setOnClickListener {
            finish()
        }

        shareButton.setOnClickListener {
            // 分享功能
        }

        favoriteButton.setOnClickListener {
            // 收藏功能
        }

        recognizeAgainButton.setOnClickListener {
            // 跳转到图像识别页面
            val intent = Intent(this, ImageUploadActivity::class.java)
            startActivity(intent)
            finish()
        }
    }

}