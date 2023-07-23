# asyncio

## Transport와 Protocol

- Transport: 네트워크 연결을 추상화한 객체 (바이트들 어떻게 전송할지) -> how
- Protocol: 데이터를 추상화한 객체 (어떤 바이트들을 전송할지) -> which

> A different way of saying the same thing: a transport is an abstraction for a socket (or similar I/O endpoint) while a protocol is an abstraction for an application, from the transport’s point of view.

위의 두 용어를 다르게 표현하면, transport는 socket(또는 비슷한 I/O endpoint)의 추상화이고, protocol은 application의 추상화이다.

Transport와 Protocol 객체는 항상 1:1 관계이다.

- 프로토콜은 데이터를 전송하기 위해 transport 객체의 메서드를 사용한다.
- 트랜스포트는 수신받은 데이터를 전달하기 위해 프로토콜 객체의 메서드를 사용한다.


### Transport

트랜스포트는 asyncio 라이브러리에서 다양한 통신 채널을 추상화하기위해 제공되는 클래스들이다. 트랜스포트 객체는 항상 asyncio의 이벤트 루프에의해 초기화된다.

asyncio는 다음과 같은 트랜스포트를 구현했다.

- TCP
- UDP
- SSL
- subprocess pipes

트랜스포트의 종류에 따라서 사용가능한 메서드들이 다르다.
트랜스포트 클래스는 스레드 안전하지 않다. 따라서 트랜스포트 객체의 메서드는 항상 asyncio의 이벤트 루프에 의해 호출되어야 한다.


#### Transport 계층

`class asyncio.BaseTransport`

모든 트랜스포트의 베이스 클래스이다. 모든 asyncio 트랜스포트가 공유하는 메서드를 포함한다.

```python
class BaseTransport:
    """Base class for transports."""

    __slots__ = ('_extra',)

    def __init__(self, extra=None):
        if extra is None:
            extra = {}
        self._extra = extra

    def get_extra_info(self, name, default=None):
        """Get optional transport information."""
        return self._extra.get(name, default)

    def is_closing(self):
        """Return True if the transport is closing or closed."""
        raise NotImplementedError

    def close(self):
        """Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError

    def set_protocol(self, protocol):
        """Set a new protocol."""
        raise NotImplementedError

    def get_protocol(self):
        """Return the current protocol."""
        raise NotImplementedError
```

`class asyncio.WriteTransport(BaseTransport)`

쓰기 전용 연결을 위한 베이스 트랜스포트이다.

WriteTransport 클래스의 인스턴스는 loop.connect_write_pipe() 이벤트 루프 메서드에 의해 반환되고, 또한 loop.subprocess_exec()와 같은 서브프로세스 관련 메서드에 의해 사용된다.

```python
class WriteTransport(BaseTransport):
    """Interface for write-only transports."""

    __slots__ = ()

    def set_write_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for write flow control.

        These two values control when to call the protocol's
        pause_writing() and resume_writing() methods.  If specified,
        the low-water limit must be less than or equal to the
        high-water limit.  Neither value can be negative.

        The defaults are implementation-specific.  If only the
        high-water limit is given, the low-water limit defaults to an
        implementation-specific value less than or equal to the
        high-water limit.  Setting high to zero forces low to zero as
        well, and causes pause_writing() to be called whenever the
        buffer becomes non-empty.  Setting low to zero causes
        resume_writing() to be called only once the buffer is empty.
        Use of zero for either limit is generally sub-optimal as it
        reduces opportunities for doing I/O and computation
        concurrently.
        """
        raise NotImplementedError

    def get_write_buffer_size(self):
        """Return the current size of the write buffer."""
        raise NotImplementedError

    def get_write_buffer_limits(self):
        """Get the high and low watermarks for write flow control.
        Return a tuple (low, high) where low and high are
        positive number of bytes."""
        raise NotImplementedError

    def write(self, data):
        """Write some data bytes to the transport.

        This does not block; it buffers the data and arranges for it
        to be sent out asynchronously.
        """
        raise NotImplementedError

    def writelines(self, list_of_data):
        """Write a list (or any iterable) of data bytes to the transport.

        The default implementation concatenates the arguments and
        calls write() on the result.
        """
        data = b''.join(list_of_data)
        self.write(data)

    def write_eof(self):
        """Close the write end after flushing buffered data.

        (This is like typing ^D into a UNIX program reading from stdin.)

        Data may still be received.
        """
        raise NotImplementedError

    def can_write_eof(self):
        """Return True if this transport supports write_eof(), False if not."""
        raise NotImplementedError

    def abort(self):
        """Close the transport immediately.

        Buffered data will be lost.  No more data will be received.
        The protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError
```

`class asyncio.ReadTransport(BaseTransport)`

읽기 전용 연결을 위한 베이스 트랜스포트이다.

ReadTransport 클래스의 인스턴스는 loop.connect_read_pipe() 이벤트 루프 메서드에 의해 반환되고, 또한 loop.subprocess_exec()와 같은 서브프로세스 관련 메서드에 의해 사용된다.

```python
class ReadTransport(BaseTransport):
    """Interface for read-only transports."""

    __slots__ = ()

    def is_reading(self):
        """Return True if the transport is receiving."""
        raise NotImplementedError

    def pause_reading(self):
        """Pause the receiving end.

        No data will be passed to the protocol's data_received()
        method until resume_reading() is called.
        """
        raise NotImplementedError

    def resume_reading(self):
        """Resume the receiving end.

        Data received will once again be passed to the protocol's
        data_received() method.
        """
        raise NotImplementedError
```

`class asyncio.Transport(WriteTransport, ReadTransport)`

TCP 연결과 같은, 양방향 트랜스포트(전송)를 나타내는 인터페이스이다.

사용자는 트랜스포트를 직접 인스턴스화하지 않는다. 대신, 프로토콜 팩토리와 트랜스포트와 프로토콜을 생성하기 위해 필요한 다른 정보를 전달하는 유틸리티 함수를 호출한다.

트랜스포트 클래스의 인스턴스는 loop.create_connection(), loop.create_unix_connection(), loop.create_server(), loop.sendfile()와 같은 이벤트 루프 메서드에 의해 반환되거나 사용된다.

```python
class Transport(ReadTransport, WriteTransport):
    """Interface representing a bidirectional transport.

    There may be several implementations, but typically, the user does
    not implement new transports; rather, the platform provides some
    useful transports that are implemented using the platform's best
    practices.

    The user never instantiates a transport directly; they call a
    utility function, passing it a protocol factory and other
    information necessary to create the transport and protocol.  (E.g.
    EventLoop.create_connection() or EventLoop.create_server().)

    The utility function will asynchronously create a transport and a
    protocol and hook them up by calling the protocol's
    connection_made() method, passing it the transport.

    The implementation here raises NotImplemented for every method
    except writelines(), which calls write() in a loop.
    """

    __slots__ = ()
```

`class asyncio.DatagramTransport(BaseTransport)`

데이터그램(UDP) 연결을 위한 트랜스포트이다.

DatagramTransport 클래스의 인스턴스는 loop.create_datagram_endpoint() 이벤트 루프 메서드에 의해 반환된다.

```python
class DatagramTransport(BaseTransport):
    """Interface for datagram (UDP) transports."""

    __slots__ = ()

    def sendto(self, data, addr=None):
        """Send data to the transport.

        This does not block; it buffers the data and arranges for it
        to be sent out asynchronously.
        addr is target socket address.
        If addr is None use target address pointed on transport creation.
        """
        raise NotImplementedError

    def abort(self):
        """Close the transport immediately.

        Buffered data will be lost.  No more data will be received.
        The protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError
```



`class asyncio.SubprocessTransport(BaseTransport)`

부모와 자식 프로세스 사이의 연결을 나타내는 추상화이다.

SubprocessTransport 클래스의 인스턴스는 loop.subprocess_shell()와 loop.subprocess_exec() 이벤트 루프 메서드에 의해 반환된다.

```python
class SubprocessTransport(BaseTransport):

    __slots__ = ()

    def get_pid(self):
        """Get subprocess id."""
        raise NotImplementedError

    def get_returncode(self):
        """Get subprocess returncode.

        See also
        http://docs.python.org/3/library/subprocess#subprocess.Popen.returncode
        """
        raise NotImplementedError

    def get_pipe_transport(self, fd):
        """Get transport for pipe with number fd."""
        raise NotImplementedError

    def send_signal(self, signal):
        """Send signal to subprocess.

        See also:
        docs.python.org/3/library/subprocess#subprocess.Popen.send_signal
        """
        raise NotImplementedError

    def terminate(self):
        """Stop the subprocess.

        Alias for close() method.

        On Posix OSs the method sends SIGTERM to the subprocess.
        On Windows the Win32 API function TerminateProcess()
         is called to stop the subprocess.

        See also:
        http://docs.python.org/3/library/subprocess#subprocess.Popen.terminate
        """
        raise NotImplementedError

    def kill(self):
        """Kill the subprocess.

        On Posix OSs the function sends SIGKILL to the subprocess.
        On Windows kill() is an alias for terminate().

        See also:
        http://docs.python.org/3/library/subprocess#subprocess.Popen.kill
        """
        raise NotImplementedError
```


## Reference
- https://docs.python.org/3/library/asyncio-protocol.html