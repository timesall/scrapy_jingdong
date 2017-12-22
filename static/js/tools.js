/*创建一个函数，用来执行一些简单的动画效果*/
/*
 * 参数：
 * 	obj 要执行动画的对象
 * 	attr 执行动画时要修改的样式(top left width height)
 * 	target 执行动画的目标
 *  speed 执行动画的速度
 * 		- 用户总是传递一个正值，然后在函数中来判断速度的正负
 * 	callback 回调函数
 * 		- 这个函数会在动画执行完毕后调用，只会调用一次
 */
function move(obj, attr, target, speed, callback) {

	//获取元素当前的位置
	//var current = obj.offsetLeft;

	//获取要修改的样式的当前的值
	var current = parseInt(getStyle(obj, attr));

	//为了move函数，有更大通用性，这里不应该使用offsetLeft，应该使用一个更加灵活的方法

	//如果当前位置（current） < 目标位置（target） 速度为正
	//如果当前位置（current） > 目标位置（target） 速度为负
	if(current > target) {
		speed = -speed;
	}

	/*
	 * 目前我们的定时器的标识使用一个全局的变量timer来保存，
	 * 	无论页面中有几个元素在执行动画，使用的都是同一个timer
	 * 	也就是一个动画在执行时，必然会关闭前一个
	 * 
	 * 注意：我们不能使用一个公共的变量去保存定时器的标识
	 */

	//关闭当前元素上的其他定时器
	clearInterval(obj.timer);

	//点击btn01，使box1向左移动
	//开启一个定时器，来控制box1的移动
	obj.timer = setInterval(function() {

		//获取box1的left属性值
		//var oldValue = obj.offsetLeft;
		var oldValue = parseInt(getStyle(obj, attr));

		//修改left值
		var newValue = oldValue + speed;

		// 0 -> 800 右
		// 800 -> 0 左
		//判断
		//如果元素从左 向 右移动，值越来越大 newValue > target
		//如果元素从右向左移动，值越来越小 newValue < target
		if((speed < 0 && newValue < target) || (speed > 0 && newValue > target)) {
			newValue = target;
		}

		//修改box1的left值
		obj.style[attr] = newValue + "px";

		//当box1运行到800px的位置时，停止移动
		if(newValue == target) {
			clearInterval(obj.timer);

			//调用回调函数
			callback && 　callback();
		}

	}, 30);
}

/*
 * 	自定一个函数，可以支持所有的浏览器，用于获取元素当前的样式
 * 		参数：
 * 			obj 要获取样式的对象
 * 			name 要获取的样式的名字
 * 
 * 注意：使用getStyle()在IE和其他浏览器中会有一些区别
 * 		在其他浏览器中，如果获取的是没有设置的样式，则这些浏览器会自动进行计算
 * 		而IE中不会自动计算，而是直接返回默认值
 * 			
 */
function getStyle(obj, name) {

	//判断浏览器中是否含有某个对象
	if(window.getComputedStyle) {
		//主流的浏览器
		return getComputedStyle(obj, null)[name];
	} else {
		//如果是ie
		return obj.currentStyle[name];
	}

}

/*
 * 定义一个函数，专门用来向一个元素中添加指定的class
 * 	obj:要添加属性的元素
 *  cn:要添加的属性名
 */
function addClass(obj, cn) {

	if(!hasClass(obj, cn)) {
		obj.className += " " + cn;
	}

}

/*
 * 定义一个函数，检查一个元素中是否含有某个class
 */
function hasClass(obj, cn) {

	//创建一个正则表达式，用于检查class
	var reg = new RegExp("\\b" + cn + "\\b");

	return reg.test(obj.className);

}

/*
 * 删除指定元素中的指定class属性值
 */
function removeClass(obj, cn) {

	//b1 abc hello  要删除b1，就是将b1替换为 ""
	if(hasClass(obj, cn)) {
		//创建正则表达式
		var reg = new RegExp("\\b" + cn + "\\b");

		//将cn，替换为空串
		/*console.log(obj.className);
		console.log(obj.className.replace(reg , ""));*/

		obj.className = obj.className.replace(reg, "");

	}

}

/*
 * 切换元素class属性的方法
 * 	- 如果元素有该class，则删除
 * 	- 如果没有，则添加
 */
function toggleClass(obj, cn) {
	if(hasClass(obj, cn)) {
		//如果有，删除
		removeClass(obj, cn);
	} else {
		//没有，添加
		addClass(obj, cn);
	}
}