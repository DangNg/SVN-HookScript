# SVN-HookScript

pre-commit:
  tricks:
    - show message to client : echo " " >&2
    - allow commit : exit 0
    - deny commit: exit 1
    - work with current commit transaction: 
        Khi commit file thì mặc định sẽ chạy command pre-commit $repo $txn 
        với $txn là transaction mà lệnh commit đang chờ. Khi code pre-commit cần cần xác định tham số này nếu không mặc định sẽ làm việc với transaction của lần commit trước
        
