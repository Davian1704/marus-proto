// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: sensor_streaming.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Sensorstreaming {
  public static partial class SensorStreaming
  {
    static readonly string __ServiceName = "sensorstreaming.SensorStreaming";

    static readonly grpc::Marshaller<global::Sensorstreaming.CameraStreamingRequest> __Marshaller_sensorstreaming_CameraStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.CameraStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Std.Empty> __Marshaller_std_Empty = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Std.Empty.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.PointCloudStreamingRequest> __Marshaller_sensorstreaming_PointCloudStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.PointCloudStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.CompressedImageStreamingRequest> __Marshaller_sensorstreaming_CompressedImageStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.CompressedImageStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.PointCloud2StreamingRequest> __Marshaller_sensorstreaming_PointCloud2StreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.PointCloud2StreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.RadarStreamingRequest> __Marshaller_sensorstreaming_RadarStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.RadarStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.DepthStreamingRequest> __Marshaller_sensorstreaming_DepthStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.DepthStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.DvlStreamingRequest> __Marshaller_sensorstreaming_DvlStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.DvlStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.GnssStreamingRequest> __Marshaller_sensorstreaming_GnssStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.GnssStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.ImuStreamingRequest> __Marshaller_sensorstreaming_ImuStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.ImuStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.PoseStreamingRequest> __Marshaller_sensorstreaming_PoseStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.PoseStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensorstreaming.AISStreamingRequest> __Marshaller_sensorstreaming_AISStreamingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensorstreaming.AISStreamingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Std.StandardRequest> __Marshaller_std_StandardRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Std.StandardRequest.Parser.ParseFrom);

    static readonly grpc::Method<global::Sensorstreaming.CameraStreamingRequest, global::Std.Empty> __Method_StreamCameraSensor = new grpc::Method<global::Sensorstreaming.CameraStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamCameraSensor",
        __Marshaller_sensorstreaming_CameraStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> __Method_StreamLidarSensor = new grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamLidarSensor",
        __Marshaller_sensorstreaming_PointCloudStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> __Method_StreamSonarSensor = new grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamSonarSensor",
        __Marshaller_sensorstreaming_PointCloudStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.CompressedImageStreamingRequest, global::Std.Empty> __Method_StreamSonarImage = new grpc::Method<global::Sensorstreaming.CompressedImageStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamSonarImage",
        __Marshaller_sensorstreaming_CompressedImageStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> __Method_StreamPointCloud = new grpc::Method<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamPointCloud",
        __Marshaller_sensorstreaming_PointCloudStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.PointCloud2StreamingRequest, global::Std.Empty> __Method_StreamPointCloud2 = new grpc::Method<global::Sensorstreaming.PointCloud2StreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamPointCloud2",
        __Marshaller_sensorstreaming_PointCloud2StreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.RadarStreamingRequest, global::Std.Empty> __Method_StreamRadarSensor = new grpc::Method<global::Sensorstreaming.RadarStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamRadarSensor",
        __Marshaller_sensorstreaming_RadarStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.DepthStreamingRequest, global::Std.Empty> __Method_StreamDepthSensor = new grpc::Method<global::Sensorstreaming.DepthStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamDepthSensor",
        __Marshaller_sensorstreaming_DepthStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.DvlStreamingRequest, global::Std.Empty> __Method_StreamDvlSensor = new grpc::Method<global::Sensorstreaming.DvlStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamDvlSensor",
        __Marshaller_sensorstreaming_DvlStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.GnssStreamingRequest, global::Std.Empty> __Method_StreamGnssSensor = new grpc::Method<global::Sensorstreaming.GnssStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamGnssSensor",
        __Marshaller_sensorstreaming_GnssStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.ImuStreamingRequest, global::Std.Empty> __Method_StreamImuSensor = new grpc::Method<global::Sensorstreaming.ImuStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamImuSensor",
        __Marshaller_sensorstreaming_ImuStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.PoseStreamingRequest, global::Std.Empty> __Method_StreamPoseSensor = new grpc::Method<global::Sensorstreaming.PoseStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamPoseSensor",
        __Marshaller_sensorstreaming_PoseStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Sensorstreaming.AISStreamingRequest, global::Std.Empty> __Method_StreamAisSensor = new grpc::Method<global::Sensorstreaming.AISStreamingRequest, global::Std.Empty>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "StreamAisSensor",
        __Marshaller_sensorstreaming_AISStreamingRequest,
        __Marshaller_std_Empty);

    static readonly grpc::Method<global::Std.StandardRequest, global::Sensorstreaming.PointCloud2StreamingRequest> __Method_RequestPointCloud2 = new grpc::Method<global::Std.StandardRequest, global::Sensorstreaming.PointCloud2StreamingRequest>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "RequestPointCloud2",
        __Marshaller_std_StandardRequest,
        __Marshaller_sensorstreaming_PointCloud2StreamingRequest);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Sensorstreaming.SensorStreamingReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of SensorStreaming</summary>
    [grpc::BindServiceMethod(typeof(SensorStreaming), "BindService")]
    public abstract partial class SensorStreamingBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamCameraSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.CameraStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamLidarSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.PointCloudStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamSonarSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.PointCloudStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamSonarImage(grpc::IAsyncStreamReader<global::Sensorstreaming.CompressedImageStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamPointCloud(grpc::IAsyncStreamReader<global::Sensorstreaming.PointCloudStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamPointCloud2(grpc::IAsyncStreamReader<global::Sensorstreaming.PointCloud2StreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamRadarSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.RadarStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamDepthSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.DepthStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamDvlSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.DvlStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamGnssSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.GnssStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamImuSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.ImuStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamPoseSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.PoseStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> StreamAisSensor(grpc::IAsyncStreamReader<global::Sensorstreaming.AISStreamingRequest> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task RequestPointCloud2(global::Std.StandardRequest request, grpc::IServerStreamWriter<global::Sensorstreaming.PointCloud2StreamingRequest> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for SensorStreaming</summary>
    public partial class SensorStreamingClient : grpc::ClientBase<SensorStreamingClient>
    {
      /// <summary>Creates a new client for SensorStreaming</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public SensorStreamingClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for SensorStreaming that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public SensorStreamingClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected SensorStreamingClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected SensorStreamingClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.CameraStreamingRequest, global::Std.Empty> StreamCameraSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamCameraSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.CameraStreamingRequest, global::Std.Empty> StreamCameraSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamCameraSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamLidarSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamLidarSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamLidarSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamLidarSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamSonarSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamSonarSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamSonarSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamSonarSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.CompressedImageStreamingRequest, global::Std.Empty> StreamSonarImage(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamSonarImage(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.CompressedImageStreamingRequest, global::Std.Empty> StreamSonarImage(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamSonarImage, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamPointCloud(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamPointCloud(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty> StreamPointCloud(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamPointCloud, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloud2StreamingRequest, global::Std.Empty> StreamPointCloud2(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamPointCloud2(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PointCloud2StreamingRequest, global::Std.Empty> StreamPointCloud2(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamPointCloud2, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.RadarStreamingRequest, global::Std.Empty> StreamRadarSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamRadarSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.RadarStreamingRequest, global::Std.Empty> StreamRadarSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamRadarSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.DepthStreamingRequest, global::Std.Empty> StreamDepthSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamDepthSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.DepthStreamingRequest, global::Std.Empty> StreamDepthSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamDepthSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.DvlStreamingRequest, global::Std.Empty> StreamDvlSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamDvlSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.DvlStreamingRequest, global::Std.Empty> StreamDvlSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamDvlSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.GnssStreamingRequest, global::Std.Empty> StreamGnssSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamGnssSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.GnssStreamingRequest, global::Std.Empty> StreamGnssSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamGnssSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.ImuStreamingRequest, global::Std.Empty> StreamImuSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamImuSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.ImuStreamingRequest, global::Std.Empty> StreamImuSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamImuSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PoseStreamingRequest, global::Std.Empty> StreamPoseSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamPoseSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.PoseStreamingRequest, global::Std.Empty> StreamPoseSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamPoseSensor, null, options);
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.AISStreamingRequest, global::Std.Empty> StreamAisSensor(grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamAisSensor(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncClientStreamingCall<global::Sensorstreaming.AISStreamingRequest, global::Std.Empty> StreamAisSensor(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_StreamAisSensor, null, options);
      }
      public virtual grpc::AsyncServerStreamingCall<global::Sensorstreaming.PointCloud2StreamingRequest> RequestPointCloud2(global::Std.StandardRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return RequestPointCloud2(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncServerStreamingCall<global::Sensorstreaming.PointCloud2StreamingRequest> RequestPointCloud2(global::Std.StandardRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_RequestPointCloud2, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override SensorStreamingClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new SensorStreamingClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(SensorStreamingBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_StreamCameraSensor, serviceImpl.StreamCameraSensor)
          .AddMethod(__Method_StreamLidarSensor, serviceImpl.StreamLidarSensor)
          .AddMethod(__Method_StreamSonarSensor, serviceImpl.StreamSonarSensor)
          .AddMethod(__Method_StreamSonarImage, serviceImpl.StreamSonarImage)
          .AddMethod(__Method_StreamPointCloud, serviceImpl.StreamPointCloud)
          .AddMethod(__Method_StreamPointCloud2, serviceImpl.StreamPointCloud2)
          .AddMethod(__Method_StreamRadarSensor, serviceImpl.StreamRadarSensor)
          .AddMethod(__Method_StreamDepthSensor, serviceImpl.StreamDepthSensor)
          .AddMethod(__Method_StreamDvlSensor, serviceImpl.StreamDvlSensor)
          .AddMethod(__Method_StreamGnssSensor, serviceImpl.StreamGnssSensor)
          .AddMethod(__Method_StreamImuSensor, serviceImpl.StreamImuSensor)
          .AddMethod(__Method_StreamPoseSensor, serviceImpl.StreamPoseSensor)
          .AddMethod(__Method_StreamAisSensor, serviceImpl.StreamAisSensor)
          .AddMethod(__Method_RequestPointCloud2, serviceImpl.RequestPointCloud2).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, SensorStreamingBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_StreamCameraSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.CameraStreamingRequest, global::Std.Empty>(serviceImpl.StreamCameraSensor));
      serviceBinder.AddMethod(__Method_StreamLidarSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(serviceImpl.StreamLidarSensor));
      serviceBinder.AddMethod(__Method_StreamSonarSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(serviceImpl.StreamSonarSensor));
      serviceBinder.AddMethod(__Method_StreamSonarImage, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.CompressedImageStreamingRequest, global::Std.Empty>(serviceImpl.StreamSonarImage));
      serviceBinder.AddMethod(__Method_StreamPointCloud, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.PointCloudStreamingRequest, global::Std.Empty>(serviceImpl.StreamPointCloud));
      serviceBinder.AddMethod(__Method_StreamPointCloud2, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.PointCloud2StreamingRequest, global::Std.Empty>(serviceImpl.StreamPointCloud2));
      serviceBinder.AddMethod(__Method_StreamRadarSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.RadarStreamingRequest, global::Std.Empty>(serviceImpl.StreamRadarSensor));
      serviceBinder.AddMethod(__Method_StreamDepthSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.DepthStreamingRequest, global::Std.Empty>(serviceImpl.StreamDepthSensor));
      serviceBinder.AddMethod(__Method_StreamDvlSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.DvlStreamingRequest, global::Std.Empty>(serviceImpl.StreamDvlSensor));
      serviceBinder.AddMethod(__Method_StreamGnssSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.GnssStreamingRequest, global::Std.Empty>(serviceImpl.StreamGnssSensor));
      serviceBinder.AddMethod(__Method_StreamImuSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.ImuStreamingRequest, global::Std.Empty>(serviceImpl.StreamImuSensor));
      serviceBinder.AddMethod(__Method_StreamPoseSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.PoseStreamingRequest, global::Std.Empty>(serviceImpl.StreamPoseSensor));
      serviceBinder.AddMethod(__Method_StreamAisSensor, serviceImpl == null ? null : new grpc::ClientStreamingServerMethod<global::Sensorstreaming.AISStreamingRequest, global::Std.Empty>(serviceImpl.StreamAisSensor));
      serviceBinder.AddMethod(__Method_RequestPointCloud2, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Std.StandardRequest, global::Sensorstreaming.PointCloud2StreamingRequest>(serviceImpl.RequestPointCloud2));
    }

  }
}
#endregion
