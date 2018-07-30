const tbody = $('.table-tbody');

const tbodyHandles = {
  deleteHandle: function(id) {
    layer.confirm('是否要删除该类型？', {
      btn: ['确认', '取消']
    }, function(index) {
      console.log(id, index);
      layer.close(index);
    });
  }
};

tbody.click(function(e) {
  const dom =  e.target;
  const key = dom.className;

  const handle = tbodyHandles[`${key}Handle`];
  if (handle) {
    handle(dom.getAttribute('data-index'));
  }
});
