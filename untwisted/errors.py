from errno import EALREADY, EINPROGRESS, EWOULDBLOCK, ECONNRESET, EINVAL, \
ENOTCONN, ESHUTDOWN, EINTR, EISCONN, EBADF, ECONNABORTED, EPIPE, EAGAIN 

CLOSE_ERR_CODE   = (ECONNRESET, ENOTCONN, ESHUTDOWN, ECONNABORTED, EPIPE, EBADF, '')
ACCEPT_ERR_CODE  = (EWOULDBLOCK, ECONNABORTED, EAGAIN)
SEND_ERR_CODE  = (EWOULDBLOCK, EAGAIN)
RECV_ERR_CODE  = (EWOULDBLOCK, EAGAIN)


