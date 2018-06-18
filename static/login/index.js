const usernameInput = $('.username');
const passwordInput = $('.password');
const checkList = [{
  dom: usernameInput,
  key: 'username',
  msg: '请输入用户名',
  next: usernameInput.next()
}, {
  dom: passwordInput,
  key: 'password',
  msg: '请输入密码',
  next: passwordInput.next()
}];

function getData(list) {
  const data = {};

  for (let i = 0, item; item = list[i++]; ) {
    const val = item.dom.val();
    if (val == '') {
      item.dom.addClass('error-input');
      item.next && item.next.text(item.msg);
      return null;
    }
    data[item.key] = val;
  }

  return data;
}

function reset(checkItem) {
  checkItem.dom.removeClass('error-input');
  checkItem.next && checkItem.next.text('');
}

$(function() {
  $('.submit-btn').click(() => {
    const data = getData(checkList);

    if (data != null) {
      $.post('/auth/login', data, (res) => {
        console.log(res);
      });
    }
  });

  checkList.forEach((item) => {
    item.dom.focus(() => {
      reset(item);
    });
  });
});
