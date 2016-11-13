// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/user.proto at 44:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import okio.ByteString;

public final class UnfollowRequest extends Message<UnfollowRequest, UnfollowRequest.Builder> {
  public static final ProtoAdapter<UnfollowRequest> ADAPTER = new ProtoAdapter_UnfollowRequest();

  private static final long serialVersionUID = 0L;

  public static final String DEFAULT_USER_ID = "";

  @WireField(
      tag = 1,
      adapter = "com.squareup.wire.ProtoAdapter#STRING"
  )
  public final String user_id;

  public UnfollowRequest(String user_id) {
    this(user_id, ByteString.EMPTY);
  }

  public UnfollowRequest(String user_id, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.user_id = user_id;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.user_id = user_id;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof UnfollowRequest)) return false;
    UnfollowRequest o = (UnfollowRequest) other;
    return unknownFields().equals(o.unknownFields())
        && Internal.equals(user_id, o.user_id);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + (user_id != null ? user_id.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (user_id != null) builder.append(", user_id=").append(user_id);
    return builder.replace(0, 2, "UnfollowRequest{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<UnfollowRequest, Builder> {
    public String user_id;

    public Builder() {
    }

    public Builder user_id(String user_id) {
      this.user_id = user_id;
      return this;
    }

    @Override
    public UnfollowRequest build() {
      return new UnfollowRequest(user_id, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_UnfollowRequest extends ProtoAdapter<UnfollowRequest> {
    ProtoAdapter_UnfollowRequest() {
      super(FieldEncoding.LENGTH_DELIMITED, UnfollowRequest.class);
    }

    @Override
    public int encodedSize(UnfollowRequest value) {
      return (value.user_id != null ? ProtoAdapter.STRING.encodedSizeWithTag(1, value.user_id) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, UnfollowRequest value) throws IOException {
      if (value.user_id != null) ProtoAdapter.STRING.encodeWithTag(writer, 1, value.user_id);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public UnfollowRequest decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.user_id(ProtoAdapter.STRING.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public UnfollowRequest redact(UnfollowRequest value) {
      Builder builder = value.newBuilder();
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
