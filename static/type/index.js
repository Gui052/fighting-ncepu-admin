const tbody = $('.table-tbody');
const modName = 'type';

const getTr = id => (`[data-id=${id}]`);

const tbodyHandles = {
  deleteHandle(id) {
    layer.confirm('是否要删除该类型？', {
      btn: ['确认', '取消']
    }, (index) => {
      get({
        path: `${modName}/delete`,
        data: { id },
        success({ msg }) {
          getTr(id).remove();
          layer.msg(msg);
        }
      });
    });
  },
  editHandle(id) {
    layer.prompt({
      title: '请输入类型名称'
    }, (text, index) => {
      layer.close(index);
      post({
        path: `${modName}/update`,
        data: { id, name: text },
        success({ msg }) {
          layer.msg(msg);
          $('.name', getTr(id)).text(text);
        }
      });
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
