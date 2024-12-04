module.exports = require("./libs/jvm.js");
!function(){
    console.log(`这是引入的包入口,导导你的111牛魔`)
    }()


module.exports = {
    greet: function() {
        console.log('欢迎使用 noobcash!');
    }
};
// index.js

class NoobCash {
    constructor() {
        this.balance = 100; // 初始余额
    }

    // 增加余额的方法
    addFunds(amount) {
        this.balance += amount;
        console.log(`已添加金额：${amount}。当前余额：${this.balance}`);
    }

    // 支付的方法
    makePayment(amount) {
        if (amount > this.balance) {
            console.log('余额不足，交易失败。');
            return false;
        } else {
            this.balance -= amount;
            console.log(`已支付金额：${amount}。剩余余额：${this.balance}`);
            return true;
        }
    }

    // 获取当前余额
    checkBalance() {
        console.log(`当前余额：${this.balance}`);
        return this.balance;
    }
}

// 导出NoobCash类
module.exports = NoobCash;

// 打印包加载信息
console.log('noobcash 包已加载。');

