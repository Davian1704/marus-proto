// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: acoustic_transmission.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Acoustictransmission {
  public static partial class AcousticTransmission
  {
    static readonly string __ServiceName = "acoustictransmission.AcousticTransmission";

    static readonly grpc::Marshaller<global::Acoustictransmission.CommandRequest> __Marshaller_acoustictransmission_CommandRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Acoustictransmission.CommandRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Acoustictransmission.AcousticRequest> __Marshaller_acoustictransmission_AcousticRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Acoustictransmission.AcousticRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Acoustictransmission.AcousticResponse> __Marshaller_acoustictransmission_AcousticResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Acoustictransmission.AcousticResponse.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Std.Empty> __Marshaller_std_Empty = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Std.Empty.Parser.ParseFrom);

    static readonly grpc::Method<global::Acoustictransmission.CommandRequest, global::Acoustictransmission.AcousticRequest> __Method_StreamAcousticRequests = new grpc::Method<global::Acoustictransmission.CommandRequest, global::Acoustictransmission.AcousticRequest>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "StreamAcousticRequests",
        __Marshaller_acoustictransmission_CommandRequest,
        __Marshaller_acoustictransmission_AcousticRequest);

    static readonly grpc::Method<global::Acoustictransmission.AcousticResponse, global::Std.Empty> __Method_ReturnAcousticPayload = new grpc::Method<global::Acoustictransmission.AcousticResponse, global::Std.Empty>(
        grpc::MethodType.Unary,
        __ServiceName,
        "ReturnAcousticPayload",
        __Marshaller_acoustictransmission_AcousticResponse,
        __Marshaller_std_Empty);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Acoustictransmission.AcousticTransmissionReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of AcousticTransmission</summary>
    [grpc::BindServiceMethod(typeof(AcousticTransmission), "BindService")]
    public abstract partial class AcousticTransmissionBase
    {
      public virtual global::System.Threading.Tasks.Task StreamAcousticRequests(global::Acoustictransmission.CommandRequest request, grpc::IServerStreamWriter<global::Acoustictransmission.AcousticRequest> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Std.Empty> ReturnAcousticPayload(global::Acoustictransmission.AcousticResponse request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for AcousticTransmission</summary>
    public partial class AcousticTransmissionClient : grpc::ClientBase<AcousticTransmissionClient>
    {
      /// <summary>Creates a new client for AcousticTransmission</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public AcousticTransmissionClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for AcousticTransmission that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public AcousticTransmissionClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected AcousticTransmissionClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected AcousticTransmissionClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual grpc::AsyncServerStreamingCall<global::Acoustictransmission.AcousticRequest> StreamAcousticRequests(global::Acoustictransmission.CommandRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamAcousticRequests(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncServerStreamingCall<global::Acoustictransmission.AcousticRequest> StreamAcousticRequests(global::Acoustictransmission.CommandRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_StreamAcousticRequests, null, options, request);
      }
      public virtual global::Std.Empty ReturnAcousticPayload(global::Acoustictransmission.AcousticResponse request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ReturnAcousticPayload(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Std.Empty ReturnAcousticPayload(global::Acoustictransmission.AcousticResponse request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_ReturnAcousticPayload, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Std.Empty> ReturnAcousticPayloadAsync(global::Acoustictransmission.AcousticResponse request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ReturnAcousticPayloadAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Std.Empty> ReturnAcousticPayloadAsync(global::Acoustictransmission.AcousticResponse request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_ReturnAcousticPayload, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override AcousticTransmissionClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new AcousticTransmissionClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(AcousticTransmissionBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_StreamAcousticRequests, serviceImpl.StreamAcousticRequests)
          .AddMethod(__Method_ReturnAcousticPayload, serviceImpl.ReturnAcousticPayload).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, AcousticTransmissionBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_StreamAcousticRequests, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Acoustictransmission.CommandRequest, global::Acoustictransmission.AcousticRequest>(serviceImpl.StreamAcousticRequests));
      serviceBinder.AddMethod(__Method_ReturnAcousticPayload, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Acoustictransmission.AcousticResponse, global::Std.Empty>(serviceImpl.ReturnAcousticPayload));
    }

  }
}
#endregion
