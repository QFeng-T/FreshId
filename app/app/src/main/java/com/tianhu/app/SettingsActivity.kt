package com.tianhu.app

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.RelativeLayout
import android.widget.Switch
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class SettingsActivity : AppCompatActivity() {

    private lateinit var backButton: Button
    private lateinit var languageItem: RelativeLayout
    private lateinit var languageValue: TextView
    private lateinit var autoSaveItem: RelativeLayout
    private lateinit var autoSaveSwitch: Switch
    private lateinit var aboutItem: RelativeLayout
    private lateinit var updateItem: RelativeLayout
    private lateinit var versionValue: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)

        // 初始化视图
        backButton = findViewById(R.id.backButton)
        languageItem = findViewById(R.id.languageItem)
        languageValue = findViewById(R.id.languageValue)
        autoSaveItem = findViewById(R.id.autoSaveItem)
        autoSaveSwitch = findViewById(R.id.autoSaveSwitch)
        aboutItem = findViewById(R.id.aboutItem)
        updateItem = findViewById(R.id.updateItem)
        versionValue = findViewById(R.id.versionValue)

        // 设置点击事件
        backButton.setOnClickListener {
            finish()
        }

        languageItem.setOnClickListener {
            // 语言设置
        }

        autoSaveSwitch.setOnCheckedChangeListener { _, isChecked ->
            // 自动保存历史设置
        }

        aboutItem.setOnClickListener {
            // 关于我们
        }

        updateItem.setOnClickListener {
            // 检查更新
        }
    }

}