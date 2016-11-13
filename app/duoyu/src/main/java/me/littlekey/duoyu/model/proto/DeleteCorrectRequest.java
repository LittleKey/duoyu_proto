// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/correct.proto at 33:1
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

public final class DeleteCorrectRequest extends Message<DeleteCorrectRequest, DeleteCorrectRequest.Builder> {
  public static final ProtoAdapter<DeleteCorrectRequest> ADAPTER = new ProtoAdapter_DeleteCorrectRequest();

  private static final long serialVersionUID = 0L;

  public static final String DEFAULT_CORRECT_ID = "";

  @WireField(
      tag = 1,
      adapter = "com.squareup.wire.ProtoAdapter#STRING"
  )
  public final String correct_id;

  public DeleteCorrectRequest(String correct_id) {
    this(correct_id, ByteString.EMPTY);
  }

  public DeleteCorrectRequest(String correct_id, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.correct_id = correct_id;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.correct_id = correct_id;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof DeleteCorrectRequest)) return false;
    DeleteCorrectRequest o = (DeleteCorrectRequest) other;
    return unknownFields().equals(o.unknownFields())
        && Internal.equals(correct_id, o.correct_id);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + (correct_id != null ? correct_id.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (correct_id != null) builder.append(", correct_id=").append(correct_id);
    return builder.replace(0, 2, "DeleteCorrectRequest{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<DeleteCorrectRequest, Builder> {
    public String correct_id;

    public Builder() {
    }

    public Builder correct_id(String correct_id) {
      this.correct_id = correct_id;
      return this;
    }

    @Override
    public DeleteCorrectRequest build() {
      return new DeleteCorrectRequest(correct_id, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_DeleteCorrectRequest extends ProtoAdapter<DeleteCorrectRequest> {
    ProtoAdapter_DeleteCorrectRequest() {
      super(FieldEncoding.LENGTH_DELIMITED, DeleteCorrectRequest.class);
    }

    @Override
    public int encodedSize(DeleteCorrectRequest value) {
      return (value.correct_id != null ? ProtoAdapter.STRING.encodedSizeWithTag(1, value.correct_id) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, DeleteCorrectRequest value) throws IOException {
      if (value.correct_id != null) ProtoAdapter.STRING.encodeWithTag(writer, 1, value.correct_id);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public DeleteCorrectRequest decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.correct_id(ProtoAdapter.STRING.decode(reader)); break;
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
    public DeleteCorrectRequest redact(DeleteCorrectRequest value) {
      Builder builder = value.newBuilder();
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
