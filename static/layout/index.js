const noop = () => {};

function request({ method, path, data, success = noop, fail = noop }) {
  $[method](`./${path}`, data, (res) => {
    if (res.code === 200) {
      success(res);
    } else {
      fail(res);
    }
  });
}

function get(params) {
  request(Object.assign(params, {
    method: 'get'
  }));
}

function post(params) {
  request(Object.assign(params, {
    method: 'post'
  }));
}
