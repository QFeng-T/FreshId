package com.tianhu.app

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class HistoryActivity : AppCompatActivity() {

    private lateinit var backButton: Button
    private lateinit var clearButton: Button
    private lateinit var historyRecyclerView: RecyclerView
    private lateinit var emptyState: LinearLayout
    private lateinit var goToScanButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_history)

        // 初始化视图
        backButton = findViewById(R.id.backButton)
        clearButton = findViewById(R.id.clearButton)
        historyRecyclerView = findViewById(R.id.historyRecyclerView)
        emptyState = findViewById(R.id.emptyState)
        goToScanButton = findViewById(R.id.goToScanButton)

        // 设置点击事件
        backButton.setOnClickListener {
            finish()
        }

        clearButton.setOnClickListener {
            // 清空历史记录
        }

        goToScanButton.setOnClickListener {
            // 跳转到图像识别页面
            val intent = Intent(this, ImageUploadActivity::class.java)
            startActivity(intent)
        }

        // 初始化RecyclerView
        historyRecyclerView.layoutManager = LinearLayoutManager(this)
        
        // 模拟加载历史记录
        loadHistory()
    }

    private fun loadHistory() {
        // 模拟空状态
        emptyState.visibility = LinearLayout.VISIBLE
        historyRecyclerView.visibility = RecyclerView.GONE
    }

}