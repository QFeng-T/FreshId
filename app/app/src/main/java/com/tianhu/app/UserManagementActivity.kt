package com.tianhu.app

import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import android.widget.ProgressBar
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.floatingactionbutton.FloatingActionButton

class UserManagementActivity : AppCompatActivity() {

    private lateinit var backButton: Button
    private lateinit var userRecyclerView: RecyclerView
    private lateinit var emptyState: LinearLayout
    private lateinit var progressBar: ProgressBar
    private lateinit var addUserButton: FloatingActionButton

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_user_management)

        // 初始化视图
        backButton = findViewById(R.id.backButton)
        userRecyclerView = findViewById(R.id.userRecyclerView)
        emptyState = findViewById(R.id.emptyState)
        progressBar = findViewById(R.id.progressBar)
        addUserButton = findViewById(R.id.addUserButton)

        // 设置点击事件
        backButton.setOnClickListener {
            finish()
        }

        addUserButton.setOnClickListener {
            // 这里可以添加创建用户的逻辑
        }

        // 初始化RecyclerView
        userRecyclerView.layoutManager = LinearLayoutManager(this)
        
        // 模拟加载用户列表
        loadUsers()
    }

    private fun loadUsers() {
        // 显示加载动画
        progressBar.visibility = ProgressBar.VISIBLE

        // 模拟加载过程
        Thread {
            Thread.sleep(1500) // 模拟网络延迟
            runOnUiThread {
                progressBar.visibility = ProgressBar.GONE
                
                // 模拟空状态
                emptyState.visibility = LinearLayout.VISIBLE
                userRecyclerView.visibility = RecyclerView.GONE
            }
        }.start()
    }

}