const tbody = $('.table-tbody');
const modName = 'type';

const getTr = id => $(`[data-id=${id}]`);

function basePrompt(cb) {
  layer.prompt({
    title: '请输入类型名称'
  }, (text, index) => {
    layer.close(index);
    cb(text);
  });
}

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
    basePrompt((text) => {
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

tbody.click((e) => {
  const dom =  e.target;
  const key = dom.className;

  const handle = tbodyHandles[`${key}Handle`];
  if (handle) {
    handle(dom.getAttribute('data-index'));
  }
});

$('.add-type').click((e) => {
  basePrompt((text) => {
    post({
      path: `${modName}/add`,
      data: { name: text },
      success({ data }) {
        const { id, msg } = data;
        $('.table-tbody').append(
          `
            <tr class="tbody-tr" data-id="${id}">
              <td>${id}</td>
              <td class="name">${text}</td>
              <td>
                <a data-index="${id}" class="delete">删除</a>
                <a data-index="${id}" class="edit">编辑</a>
              </td>
            </tr>
          `
        );
        layer.msg(msg);
      },
      fail({ msg }) {
        layer.msg(msg);
      }
    });
  });
});
