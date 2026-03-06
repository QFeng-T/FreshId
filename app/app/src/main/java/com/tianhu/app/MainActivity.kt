package com.tianhu.app

import android.content.Intent
import android.os.Bundle
import android.widget.RelativeLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.cardview.widget.CardView
import com.google.android.material.bottomnavigation.BottomNavigationView

class MainActivity : AppCompatActivity() {

    private lateinit var imageRecognitionCard: CardView
    private lateinit var historyCard: CardView
    private lateinit var userManagementCard: CardView
    private lateinit var settingsCard: CardView
    private lateinit var userAvatar: RelativeLayout
    private lateinit var bottomNav: BottomNavigationView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 初始化视图
        imageRecognitionCard = findViewById(R.id.imageRecognitionCard)
        historyCard = findViewById(R.id.historyCard)
        userManagementCard = findViewById(R.id.userManagementCard)
        settingsCard = findViewById(R.id.settingsCard)
        userAvatar = findViewById(R.id.userAvatar)
        bottomNav = findViewById(R.id.bottomNav)

        // 设置卡片点击事件
        imageRecognitionCard.setOnClickListener {
            startActivity(Intent(this, ImageUploadActivity::class.java))
        }

        historyCard.setOnClickListener {
            startActivity(Intent(this, HistoryActivity::class.java))
        }

        userManagementCard.setOnClickListener {
            // 暂时跳转到设置页面
            startActivity(Intent(this, SettingsActivity::class.java))
        }

        settingsCard.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
        }

        userAvatar.setOnClickListener {
            // 暂时跳转到设置页面
            startActivity(Intent(this, SettingsActivity::class.java))
        }

        // 设置底部导航栏点击事件
        bottomNav.setOnItemSelectedListener {
            when (it.itemId) {
                R.id.nav_home -> {
                    // 已经在首页，无需操作
                    true
                }
                R.id.nav_scan -> {
                    startActivity(Intent(this, ImageUploadActivity::class.java))
                    true
                }
                R.id.nav_history -> {
                    startActivity(Intent(this, HistoryActivity::class.java))
                    true
                }
                R.id.nav_settings -> {
                    startActivity(Intent(this, SettingsActivity::class.java))
                    true
                }
                else -> false
            }
        }
    }

}